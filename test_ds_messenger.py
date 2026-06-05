# Maya Salama
# salamam2@uci.edu
# 74793795

import ds_messenger


def test_direct_messenger_init():
    dm = ds_messenger.DirectMessenger("localhost", "testuser", "testpass")
    assert dm.token is not None


def test_send():
    dm = ds_messenger.DirectMessenger("localhost", "testuser", "testpass")
    result = dm.send("Hello!", "testuser")
    assert result is True


def test_retrieve_new():
    dm = ds_messenger.DirectMessenger("localhost", "testuser", "testpass")
    result = dm.retrieve_new()
    assert isinstance(result, list)


def test_retrieve_all():
    dm = ds_messenger.DirectMessenger("localhost", "testuser", "testpass")
    result = dm.retrieve_all()
    assert isinstance(result, list)