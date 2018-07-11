# coding: utf8
import requests

from core import (Settings, create_obj_from_json)
from exceptions import (AuthorizationException, AccountIdException)
from .schemas import CreateSuscriberSchema


class Subscribers(object):

    def __init__(self, **kwargs):

        self.settings = Settings(**kwargs)
        self.headers = self.settings.headers

    def create(self, **kwargs):

        account_id = kwargs.get('account_id', None)
        if account_id is None:
            raise AccountIdException

        url = self.settings.DRIP_BASE_URL + "{}/subscribers".format(account_id)

        data = CreateSuscriberSchema().dump(kwargs).data
        data = {
            "subscribers": [data]
        }

        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 401:
            raise AuthorizationException

        response = create_obj_from_json("subscribers", response.json())

        return response
