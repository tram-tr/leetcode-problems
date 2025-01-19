# https://leetcode.com/problems/time-based-key-value-store/description/

class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.dict.get(key, [])
        if not values:
            return ""

        left = 0
        right = len(values) - 1

        while left < right:
            mid = left + (right - left) // 2
        
            if values[mid][1] > timestamp:
                right = mid
            else:
                left = mid + 1

        if values[left][1] > timestamp:
            left -= 1

        return values[left][0] if values[left][1] <= timestamp else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
