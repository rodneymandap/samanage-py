from samanage import Samanage

class Incident(Samanage):
    def __init__(self):
        pass

    def get_incident(self, id=None):
        """
            Return a single incident
        """
        pass

    def get_all_incidents(self, **params):
        """
            Return all incidents based on the url provided.
        """
        pass

    def search_incident(self, id=None, **params):
        pass

    def update_incident(self, id=None):
        pass

    def delete_incident(self, id=None):
        pass