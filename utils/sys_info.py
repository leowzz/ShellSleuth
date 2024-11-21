import os
import subprocess
from enums import ShellType


def get_current_shell() -> ShellType:
    shell_path = os.getenv("SHELL")
    if not shell_path:
        raise EnvironmentError("无法获取当前的shell路径")

    shell_name = os.path.basename(shell_path).lower()
    if shell_name == "bash":
        return ShellType.BASH
    elif shell_name == "zsh":
        return ShellType.ZSH
    else:
        raise ValueError(f"不支持的shell类型: {shell_name}")


if __name__ == "__main__":
    print(get_current_shell())
