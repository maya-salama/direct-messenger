# Starter code for assignment 3 in ICS 32 Programming
# with Software Libraries in Python

# Replace the following placeholders with your information.

# Maya Salama
# salamam2@uci.edu
# 74793795

import socket
import ds_protocol
import time


def send(server: str, port: int, username: str,
         password: str, message: str, bio: str = None):
    '''
  The send function joins a ds server and sends a message, bio, or both

  :param server: The ip address for the ICS 32 DS server.
  :param port: The port where the ICS 32 DS server is accepting connections.
  :param username: The user name to be assigned to the message.
  :param password: The password associated with the username.
  :param message: The message to be sent to the server.
  :param bio: Optional, a bio for the user.
    '''
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((server, port))
        send_file = client.makefile("w")
        recv_file = client.makefile("r")

        join_msg = ds_protocol.format_join(username, password)
        send_file.write(join_msg + "\r\n")
        send_file.flush()
        resp = recv_file.readline()

        result = ds_protocol.extract_json(resp)
        if result.status == "ok":
            post_msg = ds_protocol.format_post(
                result.token, message, time.time())
            send_file.write(post_msg + "\r\n")
            send_file.flush()
            resp = recv_file.readline()
            post_result = ds_protocol.extract_json(resp)
            if post_result.status != "ok":
                return False

            if bio is not None:
                bio_msg = ds_protocol.format_bio(
                    result.token, bio, time.time())
                send_file.write(bio_msg + "\r\n")
                send_file.flush()
                resp = recv_file.readline()
            return True
        else:
            return False
    except Exception:
        return False
