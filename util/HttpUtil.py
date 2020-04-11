import requests
import json
from common.commonData import commonData

class HttpUtil:
    def __init__(self):
        self.http = requests.session()
        self.headers = {"Content-Type": "application/json;charset=UTF-8"}

    def post(self,path,data):
        host = commonData.host
        data_json = json.dumps(data)
        self.headers['token'] = commonData.token
        response = self.http.post(url=host+path,
                                  data=data_json,
                                  headers=self.headers)

        assert response.status_code == 200
        response_json = response.text
        response_dict = json.loads(response_json)
        return response_dict
