class Solution:
    def reverse(self, x):

        s_reverse = str(x)

        if s_reverse[0] == '-':
            s_reverse = s_reverse[1:]
            s_reverse= -1* int(s_reverse[::-1])
        else:
            s_reverse= int(s_reverse[::-1])

        if s_reverse > (2**31) -1 or s_reverse < -(2**31):
            return 0
        else:
            return s_reverse

sol = Solution()
print(sol.reverse(123))
print(sol.reverse(-123))
print(sol.reverse(120))
print(sol.reverse(0))

