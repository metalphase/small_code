class Solution:
    """Constraints
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109 """

    def twoSum(self, nums, target):
        
        # store the length of the list of numbers
        length = len(nums)

        # Checking constraints on nums and target
        if length < 2 or length > 1e9:
            return -1
        elif max(nums) > 1e9 or min(nums) < -1e9:
            return -1
        elif target < -1e9 or target > 1e9:
            return -1
            
        # We will be storing our answer indices here
        result = []

        # Sort the list in ascending order
        # nums.sort()

        # We go through each number in nums
        for i in range(length):

            # and we go through each other number in nums and calculate the
            # sum
            for j in range(length):
                
                # If the sum equals the target, and the indices are not equal
                # we append them to our list of results
                if nums[i] + nums[j] == target and i != j:
                    result.append(i)
                    result.append(j)

                    # Return our result list
                    return result
        
        # We assume there is at least and at most 1 solution

class Solution_2:
    """Constraints
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109 """

    def twoSum(self, nums, target):
        
        # store the length of the list of numbers
        length = len(nums)

        # Checking constraints on nums and target
        if length < 2 or length > 1e9:
            return -1
        elif max(nums) > 1e9 or min(nums) < -1e9:
            return -1
        elif target < -1e9 or target > 1e9:
            return -1
            
        # We will be storing our answer indices here
        result = []

        # We go through each number in nums
        for i in range(length):

            # and we go through each other number in nums and calculate the
            # sum
            required_pair = target - nums[i]

            if required_pair in nums:
                
                # Lookup the index of required_pair
                j = nums.index(required_pair)

                # If we aren't using the same index twice, we append to our
                # list and return
                if i != j:
                    result.append(i)
                    result.append(j)

                    # Return our result list
                    return result
        
        # We assume there is at least and at most 1 solution
    

# Moderately Faster Solution, at least with the number of elements we are
# using in this problem
class Solution_2_Pass_Hash_Table:
    """Constraints
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109 """

    def twoSum(self, nums, target):
        
        # store the length of the list of numbers
        length = len(nums)

        # Checking constraints on nums and target
        if length < 2 or length > 1e9:
            return -1
        elif max(nums) > 1e9 or min(nums) < -1e9:
            return -1
        elif target < -1e9 or target > 1e9:
            return -1
            
        # Assign nums elements to a dictionary hash table of element: index
        # pairs
        hash_table = {nums[i]: i for i in range(length)}

        # For each i in the length of nums we check for the complement within
        # the hast table and return the pair of i and the index of the 
        # complement, if it exists.
        for i in range(length):
            complement = target - nums[i]
            if complement in hash_table.keys() and hash_table[complement] != i:
                return [i, hash_table[complement]]
        return hash_table


class Solution_1_Pass_Hash_Table:
    """Constraints
    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109 """

    def twoSum(self, nums, target):
        
        # store the length of the list of numbers
        length = len(nums)

        # Checking constraints on nums and target
        if length < 2 or length > 1e9:
            return -1
        elif max(nums) > 1e9 or min(nums) < -1e9:
            return -1
        elif target < -1e9 or target > 1e9:
            return -1
        
        hash_table = {}

        for i in range(length):
            
            complement = target - nums[i]

            if complement in hash_table.keys() and hash_table[complement] != i:
                return [i, hash_table[complement]]
            
            hash_table[nums[i]] = i




# Example 1 - Hash Table 2-Pass
nums = [2,15,7,11]
target = 9

solution = Solution_2_Pass_Hash_Table()
print(solution.twoSum(nums, target))
print("Two-Pass Solution")

# Example 1 - Hash Table 1-Pass
nums = [2,15,7,11]
target = 9

solution = Solution_1_Pass_Hash_Table()
print(solution.twoSum(nums, target))
print("One-Pass Solution")

# Example 1
nums = [2,15,7,11]
target = 9

solution = Solution_2()
print(solution.twoSum(nums, target))

# Example 2
nums = [3,2,4]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))

# Example 3
nums = [3,3]
target = 6

solution = Solution()
print(solution.twoSum(nums, target))

# Testing constraints
nums = [3,4]
target = -1e10

solution = Solution()
print(solution.twoSum(nums, target))

# Testing constraints
nums = [3,4]
target = 1e10

solution = Solution()
print(solution.twoSum(nums, target))

# Testing constraints
nums = [1e10,4]
target = 3

solution = Solution()
print(solution.twoSum(nums, target))

# Testing constraints
nums = [4]
target = 3

solution = Solution()
print(solution.twoSum(nums, target))

# Testing constraints
nums = range(int(1e10))
target = 3

solution = Solution()
print(solution.twoSum(nums, target))