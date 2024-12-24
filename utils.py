import requests
import json


DB_ENDPOINT = 'https://eyqo7a9os8.execute-api.us-east-1.amazonaws.com/research-program/Keya'


def create_get_payload(user_name: str, password: str) -> dict:

    request_data = {
        "httpMethod": "GET",
        "queryStringParameters": {
            "username": user_name,
            "password": password
        }
    }

    return request_data


def create_post_payload(user_name, password):

    request_data = {
        "httpMethod": "POST",
        "body": {
            "username": user_name,
            "password": password
        }
    }

    return request_data


def ibs_signin(data):
  r = requests.post(DB_ENDPOINT, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  response = json.loads(response)
  
  return response


def login(data: dict) -> dict:
  r = requests.get(DB_ENDPOINT, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  response = json.loads(response)

  return response