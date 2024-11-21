from dataclasses import dataclass
from enum import Enum
from typing import Optional


@dataclass
class ModelOutputFields:
    ct_label: Optional[str]  # elf, shell
    score: Optional[float]
    group: Optional[str]  # executable, code
    mime_type: Optional[str]  # application/x-executable-elf, text/x-shellscript
    magic: Optional[str]  # ELF executable, shell script
    description: Optional[str]  # ELF executable, Shell script
