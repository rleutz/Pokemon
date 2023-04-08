import requests

class ApiCall:
    def __init__(self, base_url, params, headers, api, apikey = ""):
        ''' Build api parameters and request api connection '''
        self.base_url = base_url
        self.body = params
        self.headers = headers
        self.api = api
        self.apikey = apikey

        if apikey:
            print(f"api key is {apikey}")

    def api_call():
        result = requests.get(base_url)

        return result
