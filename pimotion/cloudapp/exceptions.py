class CloudAppError(Exception):
    def __init__(self, message=None):
        super(CloudAppError, self).__init__(message)


class CloudAppHttpError(Exception):
    def __init__(self, response=None):
        message = str(response.status_code) + ': ' + response.text
        super(CloudAppHttpError, self).__init__(message)
