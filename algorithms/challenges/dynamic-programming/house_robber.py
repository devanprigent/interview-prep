"""
You are a robber planning to rob houses along a street.
Each house has a certain amount of money. You cannot rob
two adjacent houses (the alarm will trigger).

Return the maximum amount you can rob.

Example 1:
nums = [2, 7, 9, 3, 1]
→ Output: 12  # rob house 0 (2) + house 2 (9) + house 4 (1)

Example 2:
nums = [2, 1, 1, 2]
→ Output: 4  # rob house 0 (2) + house 3 (2)
"""


# dp(i) the maximum amount you can rob up to house i include
# let's say I know dp(0), dp(1), ..., dp(i-1), how can I get dp(i)
# dp(i) = max(dp(i-2), dp(i-3)) + nums[i]
# you don't need to consider the rest because they would be included anyway


def rob_house(nums: list[int]):  # O(n) space ; O(n) time
    if not nums:
        return 0

    dp = [0]*len(nums)
    for i, num in enumerate(nums):
        if i-3 >= 0:
            dp[i] = max(dp[i-2], dp[i-3]) + num
        elif i-2 >= 0:
            dp[i] = dp[i-2] + num
        else:
            dp[i] = num

    return max(dp)


"""
MANUAL EXECUTION

dp[0] = 2
i = 1; i-3 <0 
dp[1] = 7
i = 2; i-3 < 0 ; i-2 = 0
dp[2] = dp[0] + 9 = 2 + 9 = 11
i = 3; i-3 = 0
dp[3] = max(dp[1], dp[0]) + 3 = max(2,7) + 3 = 10
i = 4; i-3 = 1
dp[4] = max(dp[2], dp[1]) + 1 = max(11,7) + 1 = 12

dp=[2, 7, 11, 10, 12]
max(dp) = 12
"""

# dp(i) the maximum amount you can rob up to house i either you rob this last one or not
# dp(i) = max(dp[i-1], dp[i-2] + nums[i])


def another_rob_house(nums: list[int]):  # O(1) space ; O(n) time
    prev1, prev2 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + num)
    return prev1


nums = [2, 7, 9, 3, 1]
print(rob_house(nums))
print(another_rob_house(nums))
