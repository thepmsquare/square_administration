from typing import List, TypeAlias

from pydantic import BaseModel
from square_commons.api_utils import StandardResponse


class RegisterUsernameV0(BaseModel):
    username: str
    password: str
    admin_password: str


class LoginUsernameV0(BaseModel):
    username: str
    password: str


class RemoveAppForSelfV0(BaseModel):
    password: str


class ResetPasswordAndLoginUsingBackupCodeV0(BaseModel):
    backup_code: str
    username: str
    new_password: str
    logout_other_sessions: bool = False


class ResetPasswordAndLoginUsingResetEmailCodeV0(BaseModel):
    reset_email_code: str
    username: str
    new_password: str
    logout_other_sessions: bool = False


class UpdatePasswordV0(BaseModel):
    old_password: str
    new_password: str
    logout_other_sessions: bool = False


class RegisterUsernameV0ResponseMain(BaseModel):
    user_id: str
    username: str
    app_id: int | None
    access_token: str | None


class RegisterUsernameV0Response(BaseModel):
    main: RegisterUsernameV0ResponseMain


class LoginUsernameV0ResponseMain(BaseModel):
    user_id: str
    access_token: str


class LoginUsernameV0Response(BaseModel):
    main: LoginUsernameV0ResponseMain


class RemoveAppForSelfV0Response(BaseModel):
    main: List[int]


LogoutV0Response: TypeAlias = StandardResponse[None]


class GenerateAccessTokenV0ResponseMain(BaseModel):
    access_token: str


class GenerateAccessTokenV0Response(BaseModel):
    main: GenerateAccessTokenV0ResponseMain


class ResetPasswordAndLoginUsingBackupCodeV0ResponseMain(BaseModel):
    user_id: str
    access_token: str


class ResetPasswordAndLoginUsingBackupCodeV0Response(BaseModel):
    main: ResetPasswordAndLoginUsingBackupCodeV0ResponseMain


class ResetPasswordAndLoginUsingResetEmailCodeV0ResponseMain(BaseModel):
    user_id: str
    access_token: str


class ResetPasswordAndLoginUsingResetEmailCodeV0Response(BaseModel):
    main: ResetPasswordAndLoginUsingResetEmailCodeV0ResponseMain


UpdatePasswordV0Response: TypeAlias = StandardResponse[None]


class RegisterLoginGoogleV0(BaseModel):
    google_id: str
