import requests
import json

#Start by creating a GetRequester class.
# This class should be able to initialize with a string URL.

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        people = json.loads(self.get_response_body())
        return people