from abc import ABCMeta, abstractmethod
from pydantic import BaseModel, Field, EmailStr
from injector import inject

from app.domains.email import Email
from app.usecases.emails.data import EmailOutputData



class EmailCreateInputData(BaseModel):
    """
    EmailCreateInputData
    """

    id: int = Field(
        ...,
        example=1,
    )
    to: EmailStr
    message: str = Field(
        ...,
        example="Message",
    )
    subject: str = Field(
        ...,
        example="Subject",
    )


class EmailCreateInteractor(metaclass=ABCMeta):
    """
    EmailCreateInteractor
    """

    @inject
    def __init__(self):
        ...

    @abstractmethod
    def handle(self, email: EmailCreateInputData) -> EmailOutputData | None:
        """
        handle
        """
        pass


class EmailCreateInteractorImpl(EmailCreateInteractor):
    """
    EmailCreateInteractorImpl
    """
    def handle(self, email_input: EmailCreateInputData) -> EmailOutputData | None:
        """
        handle
        """
        email = Email(
            id=email_input.id,
            to=email_input.to,
            message=email_input.message,
            subject=email_input.subject,
        )

        return email