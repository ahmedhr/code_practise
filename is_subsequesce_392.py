class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if s == "":
            return True
        l = len(s)
        for i in t:
            if s[j] == i:
                j += 1
                if j >= l:
                    break
        return j == l
