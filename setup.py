from setuptools import setup, find_packages

setup(
    name="my_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests==2.31.0",
        "beautifulsoup4==4.12.2"
    ],
    extras_require={
        "dev": ["pytest"]
    },
    python_requires='>=3.10',
)
