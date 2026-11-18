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
        key_array = self.timeMap[key]
        timestamp_insert = bisect.bisect_left(key_array, timestamp, key = lambda time_val: time_val[0])
        if timestamp_insert == len(key_array):
            return key_array[-1][1]
        elif timestamp_insert == 0:
            if key_array[timestamp_insert][0] == timestamp:
                return key_array[0][1]
            else:
                return ""
        elif key_array[timestamp_insert][0] > timestamp:
            return key_array[timestamp_insert - 1][1]
        else:
            return key_array[timestamp_insert][1]
