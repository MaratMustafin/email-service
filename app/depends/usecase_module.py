from injector import Injector


from app.usecases.emails.email_create_usecase import EmailCreateInteractor, EmailCreateInteractorImpl


def email_create_interactor_injector() -> EmailCreateInteractor:
    injector = Injector()
    return injector.get(EmailCreateInteractorImpl)

