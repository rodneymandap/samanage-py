import logging

from samanage import Samanage

logger = logging.getLogger(__name__)

class Incident:
    _endpoints = {
        'incidents': '/incidents.json',
        'get_incident': '/incidents/{id}.json',
        'search': '/search.json?q={number}',
    }

    def __init__(self, parent=None, *args, **kwargs):

        if parent is None:
            raise ValueError('Parent not specified.')
        self.con = parent.con

    def search(self):
        pass

    def get(self, id, layout=None):
        """
            Return a single incident
        """
        path = 'https://api.samanage.com' + self._endpoints.get('incidents')
        if layout:
            path = path + '?layout=long'
        return self.con.get(path)

    def get_all(self, url=None, layout=None):
        """
            Return all incidents based on the url provided.
        """
        if url is None:
            path = f"{self.con.base_url}/incidents.json"
        else:
            path = f"{self.con.base_url}/{url}"

        if layout:
            path = path + '?layout=long'
        return self.con.get_all(path)

    def search(self, id=None, **params):
        pass

    def update(self, id, payload):
        path = f"{self.con.base_url}/incidents/{id}.json"
        return self.con.update(path, payload)

    def delete(self, id=None):
        path = f"{self.con.base_url}/incidents/{id}.json"
        return self.con.delete(path)