class BadRequestError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class UnauthorizedRequestError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ForbiddenRequestError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NotFoundError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ConflictError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class OverQuotaError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class ServerError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class InvalidWebhookTrigger(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


error_codes = {
    400: BadRequestError,
    401: UnauthorizedRequestError,
    403: ForbiddenRequestError,
    404: NotFoundError,
    409: ConflictError,
    429: OverQuotaError,
    500: ServerError,
    502: ServerError,
    503: ServerError,
    504: ServerError,
}


def response_to_error(response):
    error = error_codes[response.status_code]
    return error(response.content)
