class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if(key in self.store):
            self.store[key].append((timestamp,value))
        else:
            self.store[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if(key in self.store):
            ans = self.store[key]
            l = 0
            h = len(ans)-1
            mid = (l+h)//2
            while(l<=h):
                mid = (l+h)//2
                if(ans[mid][0] <= timestamp):
                    res =  ans[mid][1]
                    l = mid+1
                else:
                    h = mid-1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)