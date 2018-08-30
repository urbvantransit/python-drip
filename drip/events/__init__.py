# coding: utf8
import requests

from ..core import Settings
from ..exceptions import (AuthorizationException, AccountIdException)

from .schemas import CreateEventSchema


class Events(object):

    def __init__(self, **kwargs):

        self.settings = Settings(**kwargs)
        self.headers = self.settings.headers

    def create(self, **kwargs):

        account_id = kwargs.get('account_id', None)
        if account_id is None:
            raise AccountIdException

        url = self.settings.DRIP_BASE_URL + "{}/events".format(account_id)

        data = CreateEventSchema().dump(kwargs).data
        data = {
            "events": [data]
        }

        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 401:
            raise AuthorizationException

        return response.status_code
