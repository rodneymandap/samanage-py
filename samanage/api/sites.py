from samanage import Samanage

class Site(Samanage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.resource_url = self.options.get('site') 

    def create_site(self, payload):
        if not isinstance(payload, dict):
            raise ValueError("Payload must be a dict.")

        path = f'{self.base_url}/{self.resource_url}'
        return super().create(path, payload)

    def get_site(self):
        pass

    def get_sites(self):
        pass

    def update_site(self):
        pass

    def delete_site(self):
        pass