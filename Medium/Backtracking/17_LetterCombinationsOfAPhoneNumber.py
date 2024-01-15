class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        n_to_l = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        def generate(num, curr):
            nonlocal res
            if(len(num) ==1):
                for i in n_to_l[num[0]]:
                    res.append(curr+i)
                return
            for i in n_to_l[num[0]]:
                curr += i
                generate(num[1:], curr)
                curr = curr[:-1]
        generate(digits, "")
        return res