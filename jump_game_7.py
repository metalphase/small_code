class Solution:

    def can_jump(self, s, i, j, minJump, maxJump):

        # Save some space by evaluating if the jth character is '0'
        open_space = (s[j] == '0')

        # We make a jump to j if the distance is between the range of 
        # minJump to maxJump/s.length-1
        if j >= minJump + i and j <= min(maxJump+i, len(s)-1) and open_space:
            return True
        else:
            return False


    def canReach(self, s, minJump, maxJump):
        
        # We start at the first position i = 0
        i = 0
        j = 0
        
        # We want to try jumping until we can make it to the end of the 
        # string
        while i < len(s) - 1:
            
            # If we can complete a jump to j+1, we move our i to that position
            # otherwise we increment j by 1
            if self.can_jump(s, i,j+1,minJump,maxJump):

                i = j + 1
            else:

                j+=1
            
            # If the difference between j and i is larger than the maximum jump
            # distance, then we return false as there is no further movement 
            # possible
            if j == len(s)-1:
                return False
            elif j-i > maxJump:
                return False
        
        # Here we will have found that i reached the last character. Here 
        # we return True
        return True
        

sol = Solution()
print(sol.canReach(s = "011010", minJump = 2, maxJump = 3))
print(sol.canReach(s = "01", minJump = 1, maxJump = 1))
print(sol.canReach(s = "0000000000", minJump = 2, maxJump = 5))
