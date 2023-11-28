from apps.shared_kernel.exception import CustomException
from starlette import status

class InvalidTokenException(CustomException):
    code = status.HTTP_401_UNAUTHORIZED
    error_code = "USER__INVALID_TOKEN"
    message = "Invalid token."

class PasswordDoesNotMatchException(CustomException):
    code = status.HTTP_400_BAD_REQUEST
    error_code = "USER__PASSWORD_DOES_NOT_MATCH"
    message = "password does not match"

class AleadyRegisteredUserException(CustomException):
    code = status.HTTP_400_BAD_REQUEST
    error_code = "USER__ALREADY_REGISTERED"
    message = "email aleady registered"

class WrongLoginInfoUserException(CustomException):
    code = status.HTTP_401_UNAUTHORIZED
    error_code = "USER__LOGIN_ERROR"
    message = "Incorrect username or password"