class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        g = [0,0]
        for i in range(len(s)):
            g[ord(s[i]) - ord("0")] += 1
        base = "1"
        g[1] -= 1
        base = "0" * g[0] + base
        base = "1" * (g[1] - 1) + base
        return base