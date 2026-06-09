# ds_protocol.py

# Starter code for assignment 3 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Maya Salama
# salamam2@uci.edu
# 74793795

"""Module for formatting and parsing DS server protocol messages"""

import json
from collections import namedtuple

# Namedtuple to hold the values retrieved from json messages.

DataTuple = namedtuple('DataTuple', ['status', 'token', 'messages'])


def extract_json(json_msg: str) -> DataTuple:
    '''
  Call the json.loads function on a json string
  and convert it to a DataTuple object

    '''
    try:
        json_obj = json.loads(json_msg)
        status = json_obj['response']['type']
        token = json_obj['response'].get('token')
        messages = json_obj['response'].get('messages')
        return DataTuple(status, token, messages)
    except json.JSONDecodeError:
        print("Json cannot be decoded.")
        return None


def format_join(username, password):
    """Format a join message for the DS Server."""
    d = {"join": {"username": username, "password": password, "token": ""}}
    return json.dumps(d)


def format_post(token, entry, timestamp):
    """Format a post message for the DS Server."""
    d = {"token": token, "post": {"entry": entry, "timestamp": timestamp}}
    return json.dumps(d)


def format_bio(token, bio, timestamp):
    """Format a bio message for the DS Server."""
    d = {"token": token, "bio": {"entry": bio, "timestamp": timestamp}}
    return json.dumps(d)


def format_direct_message(token, entry, recipient, timestamp):
    """Format a direct message for the DS Server."""
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
    """Format a request for new messages from the DS Server."""
    d = {"token": token, "directmessage": "new"}
    return json.dumps(d)


def format_retrieve_all(token):
    """Format a request for all messages from the DS Server."""
    d = {"token": token, "directmessage": "all"}
    return json.dumps(d)
