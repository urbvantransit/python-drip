# coding: utf8


class BaseException(Exception):

    msg = None

    def __init__(self, msg=None):

        if not self.msg:
            self.msg = msg

        Exception.__init__(self, self.msg)


class AuthorizationException(BaseException):

    msg = "Authentication failed, check your credentials"


class AccountIdException(BaseException):

    msg = "This method needs account_id."
