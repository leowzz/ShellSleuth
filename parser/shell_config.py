from enums import get_config_file_name_by_shell, ShellType


class ShellConfigParser:
    def __init__(self, shell: ShellType):
        self.shell = shell
        self.config_file_name = get_config_file_name_by_shell(shell)

    def parse(self):
        raise NotImplementedError("Not implemented")
