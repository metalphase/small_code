class Solution:
    def maxValue(self, n, x):
        
        # We want to separate between two cases where the integer n is 
        # negative and where it is positive.
        if n[0] == '-':
            
            # We start at i =1 to bypass the negative sign
            i = 1

            length = len(n)
            end_loop = False

            # We loop while our index is within the bounds of the string
            # and we have not reached an end of loop condition
            while not end_loop and (i <= length - 1):

                # We advance our index if our current insert is larger
                # than the i'th digit in n ( we don't want to make 
                # a negative number more negative! )
                if x >= int(n[i]):
                    i+=1
                # Otherwise, we have found a place to put our insert and
                # we can stop the loop
                else:
                    end_loop = True
            
            # If we looped through the whole string, we can simply tack 
            # on the insert at the end
            if i == length:
                return n + str(x)
            # Otherwise we just splice n and insert x in between
            else:
                return n[:i] + str(x) + n[i:] 

        else:
            
            # We start at 0 since there is no negative sign
            i = 0

            length = len(n)
            end_loop = False

            # Same loop procedure as before
            while not end_loop and (i <= length - 1):
                
                # If the insert is less than the i'th digit, we move on
                # ( we want to make a positive number more positive)
                if x <= int(n[i]):
                    i += 1
                # Otherwise we have our insert location
                else:
                    end_loop = True

            if i == length:
                return n + str(x)
            else:
                return (n[:i] + str(x) + n[i:])
        

sol = Solution()
print(sol.maxValue(n = "-13", x = 2))
print(sol.maxValue(n = "99", x = 9))
print(sol.maxValue(n = "134265", x = 3))
print(sol.maxValue(n = "-123456", x = 7))
print(sol.maxValue(n = "-132", x = 3))

