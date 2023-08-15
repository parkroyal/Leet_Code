from typing import List


class Solution:
    def maxSubArray_brute(self, nums: List[int]) -> int:
        """_brute_force"""
        max_sum = nums[0]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i : j + 1]))
        return max_sum

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm
        """
        max_so_far = nums[0]
        max_ending_here = nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(nums[i], max_ending_here + nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


print(Solution().maxSubArray_brute([1, 2, -3, 4, -5, 6]))
print(Solution().maxSubArray_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray_brute([5, 4, -1, 7, 8]))
print(Solution().maxSubArray([1, 2, -3, 4, -5, 6]))
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution().maxSubArray([5, 4, -1, 7, 8]))
