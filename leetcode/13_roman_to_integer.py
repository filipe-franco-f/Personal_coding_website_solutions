class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        partial = 0
        last = s[0]
        for i in range(len(s)):
            if s[i] == last:
                partial += values[last]
            else:
                if values[last] < values[s[i]]:
                    partial *= -1
                total += partial
                last = s[i]
                partial = values[last]
        return total + partial
