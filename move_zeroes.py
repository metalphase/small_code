class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 10**4:
            return -1

        i = 0
        end_of_list = len(nums) - 1
        while i <= end_of_list:
            
            if nums[i] < -(2**31) or nums[i] > 2**31 -1:
                return -1

            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
                end_of_list -= 1
            else:
                i+=1


        return nums


sol = Solution()
print(sol.moveZeroes([0,1,0,3,12]))
print(sol.moveZeroes([0]))
