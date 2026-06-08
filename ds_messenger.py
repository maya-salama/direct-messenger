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

    def send(self, message, recipient):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.dsuserver, 3001))
            send_file = client.makefile("w")
            recv_file = client.makefile("r")
            if self.token is None:
                join_msg = ds_protocol.format_join(self.username, self.password)
                send_file.write(join_msg + "\r\n")
                send_file.flush()
                resp = recv_file.readline()
                result = ds_protocol.extract_json(resp)
                if result.status == "ok":
                    self.token = result.token
                else:
                    client.close()
                    return False
            direct_message = ds_protocol.format_direct_message(self.token, message, recipient, time.time())
            send_file.write(direct_message + "\r\n")
            send_file.flush()
            read = recv_file.readline()
            client.close()
            result = ds_protocol.extract_json(read)
            if result.status == "ok":
                return True
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
        

    def retrieve_new(self):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.dsuserver, 3001))
            send_file = client.makefile("w")
            recv_file = client.makefile("r")
            if self.token is None:
                join_msg = ds_protocol.format_join(self.username, self.password)
                send_file.write(join_msg, "\r\n")
                send_file.flush()
                resp = recv_file.readline()
                result = ds_protocol.extract_json(resp)
                if result.status == "ok":
                    self.token = result.token
                else:
                    client.close()
                    return []
            format_msg = ds_protocol.format_retrieve_new(self.token)
            send_file.write(format_msg + "\r\n")
            send_file.flush()
            read = self.recv_file.readline()
            client.close()
            result = ds_protocol.extract_json(read)
            messages = []
            if result.status == "ok" and result.messages is not None:
                for m in result.messages:
                    dm = DirectMessage()
                    dm.message = m["message"]
                    dm.recipient = m["from"]
                    dm.timestamp = m["timestamp"]
                    messages.append(dm)
            return messages
        except Exception as e:
            print(f"Error: {e}")
            return []
    

    def retrieve_all(self):
        try:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((self.dsuserver, 3001))
            send_file = client.makefile("w")
            recv_file = client.makefile("r")
            if self.token is None:
                join_msg = ds_protocol.format_join(self.username, self.password)
                send_file.write(join_msg + "\r\n")
                send_file.flush()
                resp = recv_file.readline()
                result = ds_protocol.extract_json(resp)
                if result.status == "ok":
                    self.token = result.token
                else:
                    client.close()
                    return []
            format_msg = ds_protocol.format_retrieve_all(self.token)
            send_file.write(format_msg + "\r\n")
            send_file.flush()
            read = recv_file.readline()
            client.close()
            result = ds_protocol.extract_json(read)
            messages = []
            if result.status == "ok" and result.messages is not None:
                for m in result.messages:
                    dm = DirectMessage()
                    dm.message = m["message"]
                    if "from" in m:
                        dm.recipient = m["from"]
                    else:
                        dm.recipient = m["recipient"]
                    dm.timestamp = m["timestamp"]
                    messages.append(dm)
            return messages
        except Exception as e:
            print(f"Error: {e}")
            return []