# Maya Salama
# salamam2@uci.edu
# 74793795

import socket
import ds_protocol

class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None

class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
        self.dsuserver = dsuserver
        self.username = username
        self.password = password
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.dsuserver, 3001))
            self.send_file = self.client.makefile("w")
            self.recv_file = self.client.makefile("r")
            join_msg = ds_protocol.format_join(self.username, self.password)
            self.send_file.write(join_msg + "\r\n")
            self.send_file.flush()
            resp = self.recv_file.readline()
            result = ds_protocol.extract_json(resp)
            self.token = result.token
        except Exception:
            self.token = None
