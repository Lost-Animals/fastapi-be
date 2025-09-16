class StorageServiceError(Exception):
    """
    Custom exception for errors that occur while interacting with the storage service.

    Attributes:
        status_code (int): HTTP status code returned by the storage service.
        message (str): Error message from the storage service response.
    """

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"[{status_code}] {message}")
