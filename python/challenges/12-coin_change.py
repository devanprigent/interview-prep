"""
Given a list of coin denominations and a target amount,
return a combination of coins needed to make up that amount.
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
"""

def get_max_coin(coins: list[int], target: int):
    for i in range(len(coins)-1, -1, -1):
        if coins[i] <= target:
            return coins[i]
    return -1


def greedy_solution(coins: list[int], amount: int):
    ordered_coins = sorted(coins)
    total = 0
    nb_coins = 0

    while total < amount:
        max_coin = get_max_coin(ordered_coins, amount-total)
        if max_coin == -1:
            return -1
        total+=max_coin
        nb_coins+=1

    return nb_coins


coins = [1, 5, 10]
amount = 17
print(greedy_solution(coins, amount))

coins = [2]
amount = 3
print(greedy_solution(coins, amount))

coins = [1]
amount = 0
print(greedy_solution(coins, amount))