# Maya Salama
# salamam2@uci.edu
# 74793795

import ds_messenger


def test_direct_messenger_init():
    dm = ds_messenger.DirectMessenger("127.0.0.1", "testuser", "testpass")
    assert dm.dsuserver == "127.0.0.1"
    assert dm.username == "testuser"
    assert dm.password == "testpass"
    assert dm.token is None


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


def test_send_invalid_server():
    dm = ds_messenger.DirectMessenger("invalidserver", "user", "pass")
    result = dm.send("Hello!", "someone")
    assert result is False


def test_retrieve_new_invalid_server():
    dm = ds_messenger.DirectMessenger("invalidserver", "user", "pass")
    result = dm.retrieve_new()
    assert result == []


def test_retrieve_all_invalid_server():
    dm = ds_messenger.DirectMessenger("invalidserver", "user", "pass")
    result = dm.retrieve_all()
    assert result == []
