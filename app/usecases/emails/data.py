from pydantic import BaseModel, EmailStr


class EmailOutputData(BaseModel):
    """
    EmailOutputData
    """

    id: int
    to : EmailStr
    message: str
    subject: str