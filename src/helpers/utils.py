# Help you to read the json files and provide you the JSON data
import json


def get_payload_auth():
    # Read from auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def token_headers(create_token):
    temp_token = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": temp_token
    }
    return headers


