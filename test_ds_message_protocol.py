# Maya Salama
# salamam2@uci.edu
# 74793795

import ds_protocol
import json


def test_extract_json_ok():
    msg = '{"response": {"type": "ok", "message": "Direct message sent"}}'
    result = ds_protocol.extract_json(msg)
    assert result.status == "ok"


def test_extract_json_messages():
    msg = ('{"response": {"type": "ok", "messages":'
           ' [{"message": "Hi!", "from": "markb",'
           ' "timestamp": "123"}]}}')
    result = ds_protocol.extract_json(msg)
    assert result.messages is not None
    assert result.messages[0]["from"] == "markb"


def test_extract_json_token():
    msg = '{"response": {"type": "ok", "token": "abc123"}}'
    result = ds_protocol.extract_json(msg)
    assert result.token == "abc123"


def test_extract_json_format():
    result = ds_protocol.format_retrieve_new("abc123")
    parsed = json.loads(result)
    assert parsed["token"] == "abc123"
    assert parsed["directmessage"] == "new"


def test_extract_json_error():
    msg = '{"response": {"type": "error", "message": "Invalid token"}}'
    result = ds_protocol.extract_json(msg)
    assert result.status == "error"


def test_format_post():
    result = ds_protocol.format_post("abc123", "Hello!", 12345)
    parsed = json.loads(result)
    assert parsed["token"] == "abc123"
    assert parsed["post"]["entry"] == "Hello!"


def test_format_bio():
    result = ds_protocol.format_bio("abc123", "My bio", 12345)
    parsed = json.loads(result)
    assert parsed["token"] == "abc123"
    assert parsed["bio"]["entry"] == "My bio"


def test_extract_json_invalid():
    result = ds_protocol.extract_json("not valid json")
    assert result is None
