class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        
        merge_nums = nums1 + nums2
        merge_nums.sort()

        length = len(merge_nums)

        if length % 2 == 1:
            return merge_nums[length//2]
        else:
            return (merge_nums[int((length - 1)/2)] + merge_nums[int((length + 1)/ 2)])/2


sol = Solution()
print(sol.findMedianSortedArrays([1,3], [2]))
print(sol.findMedianSortedArrays([1,2], [3,4]))
print(sol.findMedianSortedArrays([0, 0], [0, 0]))
print(sol.findMedianSortedArrays([], [1]))
print(sol.findMedianSortedArrays([2], []))
