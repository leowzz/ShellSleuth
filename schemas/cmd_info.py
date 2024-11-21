from pydantic import BaseModel


class AliasInfo(BaseModel):
    alias: str
    command: str


class ExecutableInfo(BaseModel):
    executable: str
    path: str
    file_type: str