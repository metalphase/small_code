class Solution:
    def isMatch(self, s, p):
        
        s_length = len(s)
        p_length = len(p)

        i = 0
        j = 0

        


        # Matching * operator
        if i + 1 <= p_length - 1:

            if p[i+1] == '*':

                matching  = True
                i = 0
                while matching and j < s_length :

                    if s[j] == p[i]:
                        j += 1
                    else:
                        matching = False

            i += 2
        
        print(i , j)
        if i == p_length and j == s_length:
            return True
        else:
            return False

sol = Solution()
print(sol.isMatch('aa', 'aa'))
print(sol.isMatch('aaaaaaa', 'a*'))