from typing import Optional, List

from pydantic import BaseModel, Field
from square_database_structure.square.greeting.tables import Greeting


class GetAllGreetingsV0(BaseModel):
    order_by: List[str] = Field(
        default_factory=lambda: [f"-{Greeting.greeting_datetime.name}"]
    )
    limit: Optional[int] = None
    offset: int = 0


class GetAllGreetingsV0ResponseMain(BaseModel):
    greeting_anonymous_sender_name: str | None
    user_id: str | None
    greeting_id: int
    greeting_datetime: str
    greeting_is_anonymous: bool
    greeting_text: str | None
    user_username: str | None


class GetAllGreetingsV0Response(BaseModel):
    main: List[GetAllGreetingsV0ResponseMain]
    total_count: int
