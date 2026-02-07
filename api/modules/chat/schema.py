from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    message: str

class UserQuery(BaseModel):
    query: str