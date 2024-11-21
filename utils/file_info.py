import os
import subprocess
from pathlib import Path
import mimetypes

from filetype import filetype


def is_magika_installed() -> bool:
    try:
        subprocess.run(["magika", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
    return filetype.guess_mime(file_path) or mimetypes.guess_type(file_path)[0]


if __name__ == '__main__':
    home_dir = os.path.expanduser("~")

    test_files = [os.path.join(home_dir, i) for i in os.listdir(home_dir)
                  if os.path.isfile(os.path.join(home_dir, i)) and not i.startswith('.')]

    for test_file in test_files:
        file_type = get_file_type(test_file)
        print(f"File: {test_file}, Type: {file_type}")
