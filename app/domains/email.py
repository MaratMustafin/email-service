from pydantic import BaseModel, EmailStr, Field


class EmailBase(BaseModel):
    """
    EmailBase
    """

    id: int


class Email(EmailBase):
    """
    Email
    """

    id: int | None = None
    to: EmailStr
    subject: str = Field(min_length=1)
    message: str = Field(min_length=1)