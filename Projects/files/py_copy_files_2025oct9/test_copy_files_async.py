import pytest
import asyncio
from pathlib import Path
import aiofiles.os
import os
from tempfile import TemporaryDirectory
from file_copy_async import CopyParams, AsyncFileCopier


@pytest.mark.asyncio
async def test_copy_missing_files():
    with TemporaryDirectory() as tmpdir_a, TemporaryDirectory() as tmpdir_b, TemporaryDirectory() as tmpdir_c, TemporaryDirectory() as log_dir:
        # Create files in source A and B
        file_a1 = Path(tmpdir_a) / "file1.txt"
        file_a2 = Path(tmpdir_a) / "file2.txt"
        file_b1 = Path(tmpdir_b) / "file2.txt"  # same as file_a2 to simulate existence

        async with aiofiles.open(file_a1, 'w') as f:
            await f.write("File 1 content")
        async with aiofiles.open(file_a2, 'w') as f:
            await f.write("File 2 content")
        async with aiofiles.open(file_b1, 'w') as f:
            await f.write("File 2 content")

        params = CopyParams(
            sourceFolderA=tmpdir_a,
            sourceFolderB=tmpdir_b,
            destinationFolder=tmpdir_c,
            copyFilesFlag=True,
            logFolder=log_dir
        )

        copier = AsyncFileCopier(params)
        copied_count = await copier.copy_missing_files()

        # Only file1.txt should be copied because file2.txt exists in B
        assert copied_count == 1

        copied_file = Path(tmpdir_c) / "file1.txt"

        # Destination file exists
        assert copied_file.exists()

        # Logs should be created in log folder
        copied_log = Path(log_dir) / "Copied.txt"
        exists_log = Path(log_dir) / "Exists.txt"
        assert copied_log.exists()
        assert exists_log.exists()

        # Check contents of copied log
        async with aiofiles.open(copied_log, 'r') as f:
            contents = await f.read()
        assert "file1.txt" in contents

        # Check contents of exists log
        async with aiofiles.open(exists_log, 'r') as f:
            contents = await f.read()
        assert "file2.txt" in contents
