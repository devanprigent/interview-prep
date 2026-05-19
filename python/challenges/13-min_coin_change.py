"""
Given a list of coin denominations and a target amount,
return the minimum number of coins needed to make up that amount.
If it's impossible, return -1.

Example 1:
coins = [1, 5, 10], amount = 17
→ Output: 4  # 10 + 5 + 1 + 1

Example 2:
coins = [2], amount = 3
→ Output: -1  # impossible

Example 3:
coins = [1], amount = 0
→ Output: 0

Example 4:
coins = [1, 3, 4], amount = 6
→ Output: 2 # 3+3
"""


def coin_change(coins: list[int], amount: int):
    return


coins = [1, 5, 10]
amount = 17
print(greedy_solution(coins, amount))

coins = [2]
amount = 3
print(greedy_solution(coins, amount))

coins = [1]
amount = 0
print(greedy_solution(coins, amount))

coins = [1, 3, 4]
amount = 6
print(greedy_solution(coins, amount))