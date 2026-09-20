class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) #key : list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, vals = "", self.store.get(key, [])
        l, r = 0, len(vals)-1
        while l <= r:
            m = (l + r)//2
            if vals[m][1] <= timestamp:
                res = vals[m][0]
                l = m+1 #look for more higher time.
            else:
                r = m-1
        return res
