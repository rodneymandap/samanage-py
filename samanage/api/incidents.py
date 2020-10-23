from samanage import Samanage

class Incident(Samanage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resource_url = self.options.get('incident') 

    def get_incident(self, id=None, layout=None):
        """
            Return a single incident
        """
        path = f'{self.base_url}/incidents/{str(id)}.json'
        if layout:
            path = path + '?layout=long'
        return self.get(path)

    def get_all_incidents(self, url=None, layout=None):
        """
            Return all incidents based on the url provided.
        """
        if url is None:
            path = f"{self.base_url}/{self.resource_url}"
        else:
            path = f"{self.base_url}/{url}"

        if layout:
            path = path + '?layout=long'
        return self.get_all(path)
        pass

    def search_incident(self, id=None, **params):
        pass

    def update_incident(self, id, payload):
        path = f"{self.base_url}/incidents/{id}.json"
        return self.update(path, payload)

    def delete_incident(self, id=None):
        pass