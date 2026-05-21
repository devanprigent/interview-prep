"""
Given an integer array, find the contiguous subarray
with the largest sum and return its sum.

Example 1:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
→ Output: 6  # subarray [4, -1, 2, 1]

Example 2:
nums = [1]
→ Output: 1

Example 3:
nums = [-1, -2, -3]
→ Output: -1  # single least negative element
"""

# Let's note dp[i] the largest sum with i included
# Considering I have dp[0], dp[1], ..., dp[i-1], how can I compute dp[i]
# dp[0] = nums[0]
# dp[i] = max(dp[i-1] + nums[i], nums[i])
# Example1 dp = [-2, 1, -2, 4, 3, 5, 6, 1, 4]


# Time complexity O(n) ; space complexity O(n)
def max_subarray(nums: list[int]):
    if not nums:
        return 0
    n = len(nums)
    dp = [-float('inf')]*n
    dp[0] = nums[0]

    for i in range(1, n):
        dp[i] = max(dp[i-1] + nums[i], nums[i])

    return max(dp)


# Time complexity O(n) ; space complexity O(1)
def max_subarray_o1(nums: list[int]):
    if not nums:
        return 0
    best = curr = nums[0]
    for i in range(1, len(nums)):
        curr = max(curr+nums[i], nums[i])
        best = max(best, curr)
    return best


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))
print(max_subarray_o1(nums))
