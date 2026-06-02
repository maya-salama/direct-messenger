# Maya Salama
# salamam2@uci.edu
# 74793795

class DirectMessage:
    def __init__(self):
        self.recipient = None
        self.message = None
        self.timestamp = None

class DirectMessenger:
    def __init__(self, dsuserver=None, username=None, password=None):
        self.token = None
