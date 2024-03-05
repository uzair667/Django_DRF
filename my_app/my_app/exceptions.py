from rest_framework.exceptions import APIException


class NotFoundError(Exception):
      def __init__(self, message="Not found"):
            self.message = message
            super().__init__(self.message)

class UnprocessableEntity(APIException):
    status_code = 422

    def __init__(self, detail=None):
            self.detail = detail
