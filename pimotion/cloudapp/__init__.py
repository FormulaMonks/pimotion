import requests
from requests.auth import HTTPDigestAuth
import json

from cloudapp.exceptions import CloudAppHttpError

class CloudAppAPI:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def upload(self, path):
        data = self.__get('http://my.cl.ly/items/new')
        # TODO: Do something with data['uploads_remaining']
        url = data['url']
        params = data['params']

        headers = {'accept': 'application/json'}
        response = requests.post(url, files={'file': open(path, 'rb')}, data=params, allow_redirects=False)
        uri = response.headers['location']
        data = self.__get(uri)
        return data['download_url']

    def __get(self, uri):
        headers = {'accept': 'application/json'}
        r = requests.get(uri, auth=HTTPDigestAuth(self.username, self.password),
                              headers=headers)
        if r.status_code != 200:
            raise CloudAppHttpError(response=r)
        return json.loads(r.text)
