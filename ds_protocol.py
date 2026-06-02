# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Maya Salama
# salamam2@uci.edu
# 74793795

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.

DataTuple = namedtuple('DataTuple', ['status', 'token'])


def extract_json(json_msg: str) -> DataTuple:
    '''
  Call the json.loads function on a json string
  and convert it to a DataTuple object

    '''
    try:
        json_obj = json.loads(json_msg)
        status = json_obj['response']['type']
        token = json_obj['response'].get('token')
        return DataTuple(status, token)
    except json.JSONDecodeError:
        print("Json cannot be decoded.")


def format_join(username, password):
    d = {"join": {"username": username, "password": password, "token": ""}}
    return json.dumps(d)


def format_post(token, entry, timestamp):
    d = {"token": token, "post": {"entry": entry, "timestamp": timestamp}}
    return json.dumps(d)


def format_bio(token, bio, timestamp):
    d = {"token": token, "bio": {"entry": bio, "timestamp": timestamp}}
    return json.dumps(d)


def format_direct_message(token, entry, recipient, timestamp):
    d = {
        "token": token,
        "directmessage": {
            "entry": entry,
            "recipient": recipient,
            "timestamp": timestamp
        }
    }
    return json.dumps(d)


def format_retrieve_new(token):
    d = {"token": token, "directmessage": "new"}
    return json.dumps(d)


def format_retrieve_all(token):
    d = {"token": token, "directmessage": "all"}
    return json.dumps(d)
