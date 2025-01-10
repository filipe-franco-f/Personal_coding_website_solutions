print("Hello ASS")

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = []
        for l in s:
            if not l in d:
                d.append(l)
                print(d)
            else:
                return l

sol = Solution()
strung = sol.repeatedCharacter("acdvsfvndxcscvnsd")
print(strung)
