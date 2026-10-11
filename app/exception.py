
class ShortenerException(Exception):
    pass

class NotLongUrlFoundError(ShortenerException):
    pass


class SlugAlreadyExistsError(ShortenerException):
    pass