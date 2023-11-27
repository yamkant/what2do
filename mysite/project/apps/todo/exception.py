from apps.shared_kernel.exception import CustomException

class TodoContentException(CustomException):
    message = "Content is required."