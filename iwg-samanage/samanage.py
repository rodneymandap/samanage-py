import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Samanage():
    def __init__(self, token=None):
        self.base_url = "https://api.samanage.com"

        if token is None:
            raise ValueError('Invalid Token')
        else:
            self.token = token
        
        self.headers = {
            'Accept' : 'application/vnd.samanage.v2.1+json',
            'Content-Type' : 'application/json',
            'X-Samanage-Authorization' : 'Bearer {}'.format(self.token), 
        }

    def __retry_session(self, retries=5,
                      backoff_factor=0.3,
                      status_forcelist=(500, 502, 504)):
        session = requests.Session()
        retry = Retry(
            total = retries, 
            read = retries,
            connect = retries,
            backoff_factor = backoff_factor,
            status_forcelist = status_forcelist)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

    def __next_page(self):
        pass

    def get(self, url):
        """
            Return a single object
        """
        response = self.__retry_session().get(self.base_url + url, headers=self.headers)
        return response

    def get_all(self, url):
        """
            Return a lists of objects based on the specified url
        """
        response = self.get(url)
        if not response.raise_for_status():
            try:
                paginated = response.json()
                while 'next' in response.links:
                    response = self.get(response.links['next']['url'])
                    paginated.extend(response.json())
                return paginated
            except Exception:
                return response

    def create(self, url):
        pass

    def update(self, url):
        pass

