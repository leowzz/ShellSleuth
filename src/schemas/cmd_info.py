from pydantic import BaseModel


class AliasInfo(BaseModel):
    alias: str
    command: str


class FileInfo(BaseModel):
    path: str
    file_type: str
    file_size: str
