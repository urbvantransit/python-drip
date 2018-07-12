# coding: utf8
import requests

from ..core import (Settings, create_obj_from_json)
from ..exceptions import (AuthorizationException, AccountIdException)
from ..subscribers import Subscribers

from .schemas import TagSchema


class Tags(object):

    def __init__(self, **kwargs):

        self.settings = Settings(**kwargs)
        self.headers = self.settings.headers

    def create(self, **kwargs):

        account_id = kwargs.get('account_id', None)
        if account_id is None:
            raise AccountIdException

        url = self.settings.DRIP_BASE_URL + "{}/tags".format(account_id)

        data = TagSchema().dump(kwargs).data
        data = {
            "tags": [data]
        }

        response = requests.post(url, json=data, headers=self.headers)

        if response.status_code == 401:
            raise AuthorizationException

        if response.status_code == 201:
            response = Subscribers()
            response.headers = self.headers
            response = response.list(
                account_id=account_id, email=kwargs['email'])

        return response
