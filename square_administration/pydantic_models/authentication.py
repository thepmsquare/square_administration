from pydantic import BaseModel


class RegisterUsernameV0(BaseModel):
    username: str
    password: str
    admin_password: str