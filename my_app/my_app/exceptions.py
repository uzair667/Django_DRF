from rest_framework.exceptions import APIException

class UnprocessableEntity(APIException):
    status_code = 422

    def __init__(self, detail=None):
            self.detail = detail
