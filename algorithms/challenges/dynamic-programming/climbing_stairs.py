"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1 step + 1 step
2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1 step + 1 step + 1 step
1 step + 2 steps
2 steps + 1 step

Constraints:
1 <= n <= 45
"""


"""
Input: n = 4
1+1+1+1
1+2+1
2+1+1
1+1+2
2+2
Output: 5

Input: n = 5
1+1+1+1+1
1+1+1+2
1+1+2+1
1+2+1+1
2+1+1+1
2+2+1
2+1+2
1+2+1
Output: 8

How can I reach the nth stair ?
- Either by climbing one step from the (n-1)th stair
- Or by climbing two steps from the (n-2)th stair

c(n) = c(n-1) + c(n-2)
"""


def climbing(n: int) -> int:  # O(n) time, O(n) space
    if n < 3:
        return n
    c = [1]*(n+1)
    for i in range(2, n+1):
        c[i] = c[i-1] + c[i-2]
    return c[-1]


for n in range(6):
    print(climbing(n))


"""
Follow-up question:

Can you do it in O(1) space?
"""

# To compute dp[n] we only need two values : dp[n-1] and dp[n-2]. We never look further back.
# Which means we only need two variables


def climbing_01(n: int) -> int:  # O(n) time, O(1) space
    if n < 1:
        return 0
    prev2, prev1 = 1, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev1 + prev2
    return prev1


for n in range(6):
    print(climbing_01(n))

"""
Follow-up question:

What if you could take 1, 2, or 3 steps?
"""

# To adapt to the scenario with 1,2,3 steps, we would change the recurrence to c[i] = c[i-1] + c[i-2] + c[i-3]
# Everything else stays identical.

"""
Follow-up question:

What if you're given an arbitrary set of allowed step sizes?
"""


def climbing_arbitrary(n: int, steps: list[int]) -> int:
    c = [0] * (n + 1)
    c[0] = 1
    for i in range(1, n+1):
        for step in steps:
            if i-step >= 0:
                c[i] += c[i-step]
    return c[-1]


for n in range(6):
    print(climbing_arbitrary(n, [1, 2]))
