# Maya Salama
# salamam2@uci.edu
# 74793795

import ds_protocol

def test_extract_json_ok():
    msg = '{"response": {"type": "ok", "message": "Direct message sent"}}'
    result = ds_protocol.extract_json(msg)
    assert result.status == "ok"


def test_extract_json_messages():
    pass


def test_extract_json_token():
    pass


def test_extract_json_format():
    pass


def test_extract_json_error():
    pass
