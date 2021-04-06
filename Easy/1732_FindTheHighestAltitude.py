class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        current = 0
        for i in gain:
            current += i
            if (current>highest):
                highest = current
        return highest