from setuptools import setup, find_packages

setup(
    name="shell_sleuth",
    version="0.1.0",
    description="A tool to manage private tools, shortcuts, and aliases within your shell environment.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="LeoWang",
    author_email="leolswq@163.com",
    url="https://github.com/leowzz/shell_sleuth",
    packages=find_packages(),
    install_requires=[
        "click~=8.1.7",
        "pydantic~=2.10.0",
        "pydantic-settings[toml]~=2.6.1",
        "loguru~=0.7.2",
        "filetype~=1.2.0",
    ],
    extras_require={"high_precision_filetype": ["magika~=0.5.1"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "shs = src.cli:cli",
        ],
    },
)
