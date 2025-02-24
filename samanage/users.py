import logging
from samanage import incidents

from samanage import Samanage
from samanage.incidents import IncidentRecord

logger = logging.getLogger(__name__)

class UserRecord(IncidentRecord):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)

    def __repr__(self):
        super().__repr__()
        return f"<User: {self.id}>"

class User:
    _endpoints = {
        'users': '/users.json',
        'user': '/users/{id}.json'
    }

    _required_fields = (
        'email',
    )

    user_constructor = UserRecord

    def __init__(self, parent=None, *args, **kwargs):
        if parent is None:
            raise ValueError('Parent is not specified.')
        self.con = parent.con
        self.base_url = parent.base_url

    def get(self, id, params=None):
        path = self.base_url + self._endpoints.get('user').format(id=id)
        response = self.con.get(path, params=params)

        if not response:
            return None
        data = response.json()
        return self.user_constructor(**data)

    def get_all(self, params=None):
        collections = None

        path = self.base_url + self._endpoints.get('users')
        response = self.con.get(path, params=params)
        collections = response.json()

        while 'next' in response.links:
            response = self.con.get(response.links['next']['url'], params=params if params else None) 
            collections.extend(response.json())

        if not response:
            return None
        return collections

    def update(self, id, payload):
        path = self.base_url + self._endpoints.get('user').format(id=id)

        if not isinstance(payload, dict):
            raise ValueError('Payload must be a dict.')
        return self.con.put(path, json=payload)

    def delete(self, id):
        path = self.base_url + self._endpoints.get('user').format(id=id)
        return self.con.delete(path)

