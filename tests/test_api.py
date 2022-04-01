import random
import string
import unittest

import pytest
from config.config import TestData


import api_utils
from api_utils.utils import ApiUtils


au = ApiUtils()
td = TestData()
utd = td.req_create_user(2)
print(utd)


def test_get_users(get_token):
    res = au.get_api("/public/v2/users", get_token)
    assert res.status_code == 200
    return au.cnvrt_str_json(res.text)


@pytest.mark.parametrize("name, gender, email, status", td.req_create_user(2))
def test_create_user(name, gender, email, status, get_token):
    req = td.user_req_body()
    req['name'] = name
    req['gender'] = gender
    req['email'] = email
    req['status'] = status
    print(req)
    res = au.post_api("/public/v2/users", req, get_token)
    jres = au.cnvrt_str_json(res.text)
    assert res.status_code == 201
    assert jres['name'] == name
    assert jres['gender'] == gender
    assert jres['email'] == email
    assert jres['status'] == status


@pytest.mark.parametrize("name, gender, email, status", td.req_create_user(1))
def test_create_user_wrong_token_401_statuscode(name, gender, email, status, get_token):
    req = td.user_req_body()
    req['name'] = name
    req['gender'] = gender
    req['email'] = email
    req['status'] = status
    res = au.post_api("/public/v2/users", req, "gcfcfedef925f9b5207127d64afad8e765cff8fddeae1ade14095165f89bd963")
    assert res.status_code == 401

@pytest.mark.parametrize("name, gender, email, status", td.req_create_user(1))
def test_create_user_reqdataval_422_statuscode(name, gender, email, status, get_token):
    req = td.user_req_body()
    req['name'] =''
    req['gender'] = ''
    req['email'] = ''
    req['status'] = status
    res = au.post_api("/public/v2/users", req, get_token)
    assert res.status_code == 422

def test_update_user(get_token):
    data = test_get_users(get_token)
    ran = ''.join(random.choices(string.ascii_lowercase, k=7))
    data[0]['name'] = ran
    data[0]['email'] = ran + '@testmail.com'
    res = au.patch_api("/public/v2/users/" + str(data[0]['id']), data[0], get_token)
    jres = au.cnvrt_str_json(res.text)
    assert res.status_code == 200
    assert jres['name'] == ran
    assert jres['email'] == ran + '@testmail.com'

def test_delete_user(get_token):
    data = test_get_users(get_token)
    res = au.delete_api("/public/v2/users/" + str(data[0]['id']), get_token)
    assert res.status_code == 204
    new_data = test_get_users(get_token)
    status = next((x for x in new_data if x["id"] == data[0]['id']), None)
    assert status == None












