from enum import Enum


class ShellType(str, Enum):
    BASH = "bash"
    ZSH = "zsh"


class ShellConfigFileName(str, Enum):
    BASH = ".bashrc"
    ZSH = ".zshrc"


def get_config_file_name_by_shell(shell: ShellType) -> ShellConfigFileName:
    shell_type_2_config_file_name = {
        ShellType.BASH: ShellConfigFileName.BASH,
        ShellType.ZSH: ShellConfigFileName.ZSH,
    }
    return shell_type_2_config_file_name[shell]
