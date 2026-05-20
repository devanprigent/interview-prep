"""
Given an array of integers nums, return the length of the longest strictly increasing subsequence.

A subsequence is derived by deleting zero or more elements without changing the order of the remaining elements. It does not need to be contiguous.

Example 1:
Input: [10, 9, 2, 5, 3, 7, 101, 18]
Output: 4
Explanation: One LIS is [2, 3, 7, 101].

Example 2:
Input: [0, 1, 0, 3, 2, 3]
Output: 4

Example 3:
Input: [7, 7, 7, 7]
Output: 1

Constraints:
1 <= len(nums) <= 2500
-10^4 <= nums[i] <= 10^4
"""


def length_of_lis(nums: list[int]) -> int:
    if not nums:
        return 0
    # How the calculs of a sub element could help me ?
    # Let's call dp[j] the length of the lis whose last element is num[j]
    # Now, if I know dp[0], dp[1], ..., dp[j-1], how can I use them to compute dp[j] ?
    # dp[j] = max(dp[i] + 1) for i in range(j) if nums[i] < nums[j]
    n = len(nums)
    dp = [1] * n
    for j in range(1, n):
        for i in range(j):
            if nums[i] < nums[j]:
                dp[j] = max(dp[j], dp[i]+1)
    return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))

nums = [0, 1, 0, 3, 2, 3]
print(length_of_lis(nums))

nums = [7, 7, 7, 7]
print(length_of_lis(nums))
