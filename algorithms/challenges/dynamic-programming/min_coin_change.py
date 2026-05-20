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
    # A list which represent the minimum number of coins to make up the amount i
    dp = [float('inf') for i in range(amount+1)]
    dp[0] = 0

    for i in range(1, amount+1):
        for coin in coins:
            if i-coin >= 0:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1
    

coins = [1, 5, 10]
amount = 17
print(coin_change(coins, amount))


coins = [2]
amount = 3
print(coin_change(coins, amount))

coins = [1]
amount = 0
print(coin_change(coins, amount))

coins = [1, 3, 4]
amount = 6
print(coin_change(coins, amount))
