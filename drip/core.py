# coding: utf8
import base64
import types


class Settings(object):

    DRIP_BASE_URL = "https://api.getdrip.com/v2/"

    def __init__(self, app_name='', api_key=''):

        self.app_name = app_name

        api_key = base64.b64encode(
            api_key.encode('utf-8')).decode('utf-8')

        self.headers = self._create_headers(api_key, app_name)

    def _create_headers(self, api_key, app_name):
        data = {
            "Authorization": "Basic {}".format(api_key)
        }
        if self.app_name:
            data.update({"User-Agent": app_name})
        return data


def create_obj_from_json(resource, json):
    if resource in json:
        items = json.get(resource, [])
        if items:
            obj_list = []
            for item in items:
                obj = types.SimpleNamespace()
                obj.__name__ = resource
                [setattr(obj, k, v) for k, v in item.items()]
                obj_list.append(obj)
            return obj_list
    return []
