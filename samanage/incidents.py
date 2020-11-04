import logging

from samanage import Samanage

logger = logging.getLogger(__name__)

class IncidentRecord:
    """
        TODO:  
    """
    def __init__(self, parent=None, **kwargs):
        self.con = parent
        pass
    pass

    
class Incident:
    _endpoints = {
        'incidents': '/incidents.json',
        'get_incident': '/incidents/{id}.json',
        'search': '/search.json?q={keyword}',
    }

    def __init__(self, parent=None, *args, **kwargs):

        if parent is None:
            raise ValueError('Parent not specified.')
        self.con = parent.con
        self.base_url = parent.base_url

    def get(self, id, layout=None):
        """
            Return a single incident
        """
        path = 'https://api.samanage.com' + self._endpoints.get('get_incident').format(id=id)
        if layout:
            path = path + '?layout=long'
        response = self.con.get(path)

        if not response:
            return None
        data = response.json()
        return data

    def get_all(self, url=None, layout=None):
        """
            Return all incidents based on the url provided.
        """
        collections = []

        if url is None:
            path = 'https://api.samanage.com' + self._endpoints.get('incidents')
        else:
            path = url

        response = self.con.get(path)
        collections.append(response.json())

        while 'next' in response.links:
            response = self.con.get(response.links['next']['url']) 
            collections.append(response.json())

        return collections
        
        if url is None:
            path = f"{self.base_url}/incidents.json"
        else:
            path = f"{self.base_url}/{url}"

        if layout:
            path = path + '?layout=long'
        return self.con.get_all(path)

    def search(self, keyword, **params):
        path = self.base_url + self._endpoints.get('search').format(keyword=keyword)
        self.con.get(path)

    def update(self, id, payload):
        if not isinstance(payload, dict):
            raise ValueError('Payload must be a dict.')

        path = self.base_url + self._endpoints.get('get_incident').format(id=id)
        return self.con.update(path, payload)

    def delete(self, id):
        path = self.base_url + self._endpoints.get('get_incident').format(id=id)
        return self.con.delete(path)