from typing import Tuple, Type
import os

from pydantic import BaseModel, Field

from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)


class FileInfo(BaseModel):
    file_size_unit: str = "KB"


class Settings(BaseSettings):
    """
    https://docs.pydantic.dev/latest/concepts/pydantic_settings/#other-settings-source
    """
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    app_name: str = Field("shell_sleuth", frozen=True)
    debug: bool = False
    database_url: str = "sqlite:///./cache.db"
    shell: str = "bash"

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

if __name__ == "__main__":
    print(setting)
