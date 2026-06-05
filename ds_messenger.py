# Maya Salama
# salamam2@uci.edu
# 74793795

import socket
import ds_protocol
import time

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

    def send(self, message, recipient):
        try:
            if self.token is None:
                return False
            direct_message = ds_protocol.format_direct_message(self.token, message, recipient, time.time())
            self.send_file.write(direct_message + "\r\n")
            self.send_file.flush()
            read = self.recv_file.readline()
            result = ds_protocol.extract_json(read)
            if result.status == "ok":
                return True
            else:
                return False
        except Exception:
            return False
        

    def retrieve_new(self):
        try:
            if self.token is None:
                return []
            format_msg = ds_protocol.format_retrieve_new(self.token)
            self.send_file.write(format_msg + "\r\n")
            self.send_file.flush()
            read = self.recv_file.readline()
            result = ds_protocol.extract_json(read)
            messages = []
            for m in result.messages:
                dm = DirectMessage()
                dm.message = m["message"]
                dm.recipient = m["from"]
                dm.timestamp = m["timestamp"]
                messages.append(dm)
            return messages
        except Exception:
            return []