import requests
import json


def get_request(url, auth, in_json):
    response = requests.get(url=url, auth=auth)
    if in_json is True:
        return response.json()
    return response


def post_request(url, auth, headers, payload, in_json):
    post_response_data = requests.post(url=url, headers=headers, auth=auth, data=json.dumps(payload))
    if in_json is True:
        return post_response_data.json()
    return post_response_data


def put_data(url, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def patch_data(url, headers, payload, in_json):
    patch_response_data = requests.patch(url=url, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return patch_response_data.json()
    return patch_response_data


def delete_data(url, headers):
    delete_response_data = requests.delete(url=url, headers=headers)
    return delete_response_data


def create_token(url, headers, payload, in_json):
    create_token_request = requests.post(url=url, headers=headers, data=json.dumps(payload))
    if in_json is True:
        return create_token_request.json()
    return create_token_request
