class TimeMap(object, ):

    def __init__(self):
        self.nestedDict = {}
        self.dictVals = {}
        self.prev = {}

    def set(self, key, value, timestamp):
        if (key not in self.nestedDict):
            self.nestedDict[key] = [{'timestamp': timestamp, 'value': value}]
        else:
            self.nestedDict[key].append(
                {'timestamp': timestamp, 'value': value})

    def get(self, key, timestamp):
        for v in reversed(self.nestedDict[key]):
            if (v['timestamp'] <= timestamp):
                return v['value']
        return ''
