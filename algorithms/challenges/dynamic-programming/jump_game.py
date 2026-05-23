"""
You are given an array of integer where each element
represents your maximum jump length from that position.

You start at index 0. You want to reach the last index.
At any index i, you can jump forward to any index in the 
range [i+1, i+nums[i]] — you choose.

Return True if you can reach the last index, False otherwise.

Example 1:
nums = [2, 3, 1, 1, 4]
→ Output: True  # jump 1 from index 0, then 3 from index 1

Example 2:
nums = [3, 2, 1, 0, 4]
→ Output: False  # always get stuck at index 3
"""


# I think it could work if we used a matrix of boolean
# where dp[i,j] tells you the answer to the question:
# can I get to j from i ?
# For example 1:
#       0    1    2     3     4
#   0 True  True True True True
#   1 False True  True True True
#   2 False False True  True  True
#   3 False False False True  True
#   4 False False False False True
# It wouldn't be difficult to answer the question for
# two given indices, some would be trivial to answer
# i.e. dp[i,i] = True
# for i > j dp[i,j] = False
# and you can use the answer of previously computed
# indice to compute newer ones
# dp[i,j] = (nums[i] >= j-i) OR (there is (dp[i,k] and dp[k, j]) for k in [i, j])
# At the end, you just have to return dp[0, len(nums)-1]
# to get the answer to the challenge.
# However this has a time complexity of O(n**3)
# and a space complexity of O(n**2)
# so we should try to find a better solution.

# We are computing more than necessary. We are computing reachability between every pair
# (i, j). The problem only asks one yes/no question. We could probably do it with one array.
# If we note reach[i] = "can I get from i to n-1?"
# Then the recurrence becomes :
# reach[i] = ∃ k ∈ (i, i + nums[i]] such that reach[k]
# with base case reach[n-1] = True
# filled right-to-left.
# Space complexity : O(n)
# Time complexity : O(n**2)

def jump_game(nums: list[int]):
    n = len(nums)
    reach = [False]*(n-1) + [True]

    for i in range(n-2, -1, -1):
        for k in range(i+1, min(i+nums[i]+1, n)):
            if reach[k]:
                reach[i] = True
                break

    return reach[0]


nums = [2, 3, 1, 1, 4]
print(jump_game(nums))


"""
MANUAL EXECUTION
n = 5
reach = [False, False, False, False, True]

i = n-2 = 3
range(3, 5)
k = 3
reach(3) = False
k = 4
reach(4) = True
reach(3) = True

i=n-3=2
range(2, 4)
k=2
k=3
reach(2) = True

i=n-4=1
reach(1) = True

i=n-5 = 0
"""

# We have a solution with
# Space complexity : O(n)
# Time complexity : O(n**2)
# Now, we could do better.

# We are keeping in memory the reachability between every index and n-1
# Whereas we only care about 0 and n-1
# We could start from the right and determine if that point is reachable
# by any other index before
# if so we jump at that index and keep going until it fails or we reach 0

# That would be taking the closest reachable option available at each step. It's a
# greedy approach.
# The problem with greedy approach is that an optimally local solution
# can lead you to a dead-end globally. Is it the case here ?
# Would be the case if choosing the first option available would trap
# you whereas the second option would have worked
# But wait, if the second option means has enough jumps to go to the
# current position, it also has enough jumps to go to the first option.
# Hence, choosing the first available will never trap you because it
# will be included into the next options anyway.
# That's because you can decide to do nums[i] jumps or less.
# If the instructions were saying "you have to do exactly nums[i]",
# then this greedy approach wouldn't work.


def greedy_approach(nums: list[int]):
    n = len(nums)
    curr = n-1
    for i in range(n-2, -1, -1):
        if i+nums[i] >= curr:
            curr = i
    return curr == 0
