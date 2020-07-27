class Logger(object, ):

    def __init__(self):
        start_time = 0
        self.last_vals = []
        self.info = {}

    def shouldPrintMessage(self, timestamp, message):
        for val in self.last_vals:
            if ((timestamp - self.info[val]) >= 10):
                self.last_vals.remove(val)
        if (message not in self.last_vals):
            self.info[message] = timestamp
            self.last_vals.append(message)
            return True
        else:
            return False