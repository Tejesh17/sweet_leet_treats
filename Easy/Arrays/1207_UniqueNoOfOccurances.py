class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ar_count = Counter(arr)
        return len(set(ar_count.values())) == len(ar_count.values())