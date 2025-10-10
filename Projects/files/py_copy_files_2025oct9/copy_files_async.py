import asyncio
import aiofiles
import aiofiles.os
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class CopyParams:
    sourceFolderA: str
    sourceFolderB: str
    destinationFolder: str
    copyFilesFlag: bool
    logFolder: str  # folder where logs like Copied.txt and Exists.txt are saved


class AsyncFileCopier:
    def __init__(self, params: CopyParams):
        self.params = params
        self._ensure_directories()

    def _ensure_directories(self):
        # Create destination and log folders if they do not exist
        os.makedirs(self.params.destinationFolder, exist_ok=True)
        if self.params.logFolder:
            os.makedirs(self.params.logFolder, exist_ok=True)

    async def get_files_in_folder(self, folder: str) -> List[str]:
        files = []
        try:
            async for entry in await aiofiles.os.scandir(folder):
                if entry.is_file():
                    files.append(entry.name)
        except FileNotFoundError:
            print(f"[ERROR] Folder not found: {folder}")
        return files

    async def copy_missing_files(self) -> int:
        folder_a = self.params.sourceFolderA
        folder_b = self.params.sourceFolderB
        folder_c = self.params.destinationFolder

        print(f"[DEBUG] Destination folder: {folder_c}")

        files_in_a, files_in_b, files_in_c = await asyncio.gather(
            self.get_files_in_folder(folder_a),
            self.get_files_in_folder(folder_b),
            self.get_files_in_folder(folder_c),
        )

        print(f"[DEBUG] Files in A: {files_in_a}")
        print(f"[DEBUG] Files in B: {files_in_b}")
        print(f"[DEBUG] Files in C: {files_in_c}")

        copied_files = []
        existing_files = []

        for file in files_in_a:
            if file not in files_in_b and file not in files_in_c:
                source_path = Path(folder_a) / file
                dest_path = Path(folder_c) / file

                if self.params.copyFilesFlag:
                    await self._async_copy_file(source_path, dest_path)
                    print(f"[SUCCESS] Copied: {file}")
                    copied_files.append(str(source_path))
                else:
                    print(f"[DRY RUN] Would copy: {file}")
                    copied_files.append(str(source_path))
            else:
                existing_files.append(file)
                print(f"[SKIPPED] File exists: {file}")

        # Write logs
        if self.params.logFolder:
            copied_log_path = Path(self.params.logFolder) / "Copied.txt"
            exists_log_path = Path(self.params.logFolder) / "Exists.txt"

            if copied_files:
                async with aiofiles.open(copied_log_path, 'w') as f:
                    await f.write("\n".join(copied_files))
            if existing_files:
                async with aiofiles.open(exists_log_path, 'w') as f:
                    await f.write("\n".join(existing_files))

        return len(copied_files)

    async def _async_copy_file(self, src: Path, dst: Path):
        # Async file copy by reading/writing in chunks
        chunk_size = 64 * 1024
        async with aiofiles.open(src, 'rb') as fsrc, aiofiles.open(dst, 'wb') as fdst:
            while True:
                chunk = await fsrc.read(chunk_size)
                if not chunk:
                    break
                await fdst.write(chunk)


async def load_params_from_file(file_path: str) -> CopyParams:
    async with aiofiles.open(file_path, 'r') as f:
        content = await f.read()
    data = json.loads(content)
    return CopyParams(**data)


# Example usage
async def main():
    params = await load_params_from_file("config.json")
    copier = AsyncFileCopier(params)
    copied_count = await copier.copy_missing_files()
    print(f"Copied files count: {copied_count}")


if __name__ == "__main__":
    asyncio.run(main())
