class Solution:
    def myAtoi(self, s):
        
        s = s.replace(' ', '')
        sign = 1
        
        if s[0] == '-':
            sign = -1
            s = s[1:]
        
        elif s[0] == '+':
            s = s[1:]
        
        s_length = len(s)
        end_of_read = True
        integer = ''
        i = 0
        while end_of_read and i <= s_length - 1:
            
            if not s[i].isnumeric():
                end_of_read = False
            else:
                integer += s[i]
            
            i+=1
        
        if integer == '':
            return 0
        else:
            integer = sign * int(integer)

        if integer > (2**31 - 1):
            
            integer = (2**31 - 1) 
        
        elif integer < -(2**31):
            
            integer = -(2**31)


        return integer

sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -42"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("words and 987"))
print(sol.myAtoi("   +0 123"))
