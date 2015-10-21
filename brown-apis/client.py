import requests
import json

class Client(object):
    ''' A client for interacting with Brown APIs resources '''

    prefix = 'https://'
    host = 'api.students.brown.edu'

    def __init__(self, client_id):
        if not client_id:
            raise TypeError("A client_id must be provided.")
        self.client_id = client_id

    def request(self, endpoint, **options):
        ''' Make a request to a specific endpoint with certain keyword arguments
            and receive a Python dictionary as a response

            args:   endpoint (string) - e.g. '/dining/menu', '/wifi/count', etc
                        The endpoint must begin with a '/'.
                    options (optional keyword arguments) - Any optional arguments
                        to be included in the request (not including client_id)
        '''
        args = 'client_id=' + self.client_id
        args += ''.join('&' + key + '=' + options[key] for key in options)
        url = self.prefix + self.host + endpoint + '?' + args
        response = requests.get(url).content.decode('UTF-8')

        return json.loads(response)