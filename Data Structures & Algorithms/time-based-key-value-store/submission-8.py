import bisect
class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        timestamp_insert = bisect.bisect_left(self.timeMap[key], timestamp, key = lambda time_val: time_val[0])
        if timestamp_insert == len(self.timeMap[key]):
            return self.timeMap[key][-1][1]
        elif timestamp_insert == 0:
            if self.timeMap[key][timestamp_insert][0] == timestamp:
                return self.timeMap[key][0][1]
            else:
                return ""
        elif self.timeMap[key][timestamp_insert][0] > timestamp:
            return self.timeMap[key][timestamp_insert - 1][1]
        else:
            return self.timeMap[key][timestamp_insert][1]
