import requests
import json


class ApiUtils:


    baseuri = "https://gorest.co.in/"

    def get_token(self):
        token = "fcfcfedef925f9b5207127d64afad8e765cff8fddeae1ade14095165f89bd963"
        return token

    def get_api(self, endpoint,token):
        res = requests.get(self.baseuri + endpoint, headers={'Accept': 'application/json', 'Content-Type':'application/json',
                                                             'Authorization': 'Bearer {}' .format(token)})
        return res

    def post_api(self,endpoint,req_body,token):
        res = requests.post(self.baseuri + endpoint, headers={'Accept': 'application/json', 'Content-Type':'application/json',
                            'Authorization': 'Bearer {}' .format(token)}, json=req_body)
        return res

    def patch_api(self,endpoint,req_body,token):
        res = requests.patch(self.baseuri + endpoint, headers={'Accept': 'application/json', 'Content-Type':'application/json',
                            'Authorization': 'Bearer {}' .format(token)}, json=req_body)
        return res


    def delete_api(self,endpoint,token):
        res = requests.delete(self.baseuri + endpoint, headers={'Accept': 'application/json', 'Content-Type':'application/json',
                            'Authorization': 'Bearer {}' .format(token)})
        return res

    def cnvrt_str_json(self,str):
        return json.loads(str)


# api = ApiUtils()
# print(api.get_api("/public/v2/users/3475", "fcfcfedef925f9b5207127d64afad8e765cff8fddeae1ade14095165f89bd963").text)



