from fastapi import APIRouter, status, Depends, Response
from fastapi.exceptions import HTTPException


from app.usecases.emails.data import EmailOutputData
from app.usecases.emails.email_create_usecase import EmailCreateInputData, EmailCreateInteractor

from app.core.logger import logger
from app.depends.usecase_module import email_create_interactor_injector
from app.lib.send_email import send_mail
router = APIRouter()



@router.post(
    "/send_email",
    response_model=EmailOutputData,
    status_code=status.HTTP_201_CREATED,
    responses={},
)
def create_email(
    email: EmailCreateInputData,
    email_create_interactor: EmailCreateInteractor = Depends(email_create_interactor_injector),
) -> EmailOutputData | Response:
    """
    create_email
    """
    logger.info(f"Request:create_email")
    try:
        logger.info(f"Content created...")
        content = email_create_interactor.handle(email)
        send_mail(content) # плохо
    # добавить 422
    except Exception as e:
        logger.exception(f"Exception:{e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    return content