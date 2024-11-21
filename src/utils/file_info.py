import os
import subprocess
from pathlib import Path
import mimetypes
from typing import Optional

from filetype import filetype
from loguru import logger

from src.core.config import setting
from src.enums import ShellType, ShellConfigFileName


def is_magika_installed() -> bool:
    try:
        subprocess.run(
            ["magika", "--version"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def get_file_type(file_path: str) -> str:
    if is_magika_installed():
        from magika import Magika
        from magika.types import MagikaResult

        magika = Magika()
        result: MagikaResult = magika.identify_path(Path(file_path))
        return result.output.mime_type
    if os.path.isdir(file_path):
        return "inode/directory"
    return filetype.guess_mime(file_path) or mimetypes.guess_type(file_path)[0]


def expand_file_path(file_name):
    if "~" in file_name:
        file_name = os.path.expanduser(file_name)

    return os.path.abspath(file_name)


def get_shell_config_file_path() -> Optional[str]:
    res = setting.shell_config_file_path

    res = res or {
        ShellType.BASH: ShellConfigFileName.BASH,
        ShellType.ZSH: ShellConfigFileName.ZSH,
    }.get(setting.shell, None)

    if not res:
        logger.error(f"shell_config_file not found: {setting.shell=}, {setting.shell_config_file_path=}")

    res = expand_file_path(res)

    if not os.path.exists(res):
        logger.error(f"{res=}, file not exist")

    return res


if __name__ == "__main__":
    home_dir = os.path.expanduser("~")

    test_files = [
        os.path.join(home_dir, i)
        for i in os.listdir(home_dir)
        if os.path.isfile(os.path.join(home_dir, i)) and not i.startswith(".")
    ]

    for test_file in test_files:
        file_type = get_file_type(test_file)
        print(f"File: {test_file}, Type: {file_type}")
