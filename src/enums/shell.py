from enum import Enum


class ShellType(str, Enum):
    BASH = "bash"
    ZSH = "zsh"


class ShellConfigFileName(str, Enum):
    BASH = "~/.bashrc"
    ZSH = "~/.zshrc"
