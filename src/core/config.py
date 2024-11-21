from typing import Tuple, Type, Optional
import os

from loguru import logger
from pydantic import BaseModel, Field

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

from src.enums import ShellType


class FileInfo(BaseModel):
    file_size_unit: str = "KB"


class Settings(BaseSettings):
    """
    https://docs.pydantic.dev/latest/concepts/pydantic_settings/#other-settings-source
    """
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    logger.info(f"{BASE_DIR=}")

    app_name: str = Field("shell_sleuth", frozen=True)
    debug: bool = False
    database_url: str = "sqlite:///./cache.db"
    shell: ShellType = "bash"
    shell_config_file_path: Optional[str] = None

    file_info: FileInfo

    model_config = SettingsConfigDict(toml_file=os.path.join(BASE_DIR, "config.toml"))

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: Type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> Tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)


setting = Settings()
logger.info(f"{setting=}")
if __name__ == "__main__":
    print(setting)
