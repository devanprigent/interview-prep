"""
A message was encoded by mapping 'A'→'1', 'B'→'2', ..., 'Z'→'26'.
Given a string of digits, return the number of ways to decode it.

Example 1:
s = "12"
→ Output: 2  # "AB" (1+2) or "L" (12)

Example 2:
s = "226"
→ Output: 3  # "BZ" (2+26), "VF" (22+6), "BBF" (2+2+6)

Example 3:
s = "06"
→ Output: 0  # "06" is invalid, 0 cannot be mapped

Example 4:
s = "11"
→ Output: 2  # (1+1), (11)

s = "111"
→ Output: 3  # (1+1+1), (11+1), (1+11)

s = "1111"
→ Output: 5  # (1+1+1+1), (11+1+1), (1+11+1) , (11+11), (1+1+11)

"""


def decode_ways(s: str):
    if not s or s[0] == '0':
        return 0
    n = len(s)
    dp = [0]*n
    dp[0] = 1

    for i in range(1, n):
        if s[i] != '0':
            dp[i] = dp[i-1]
        twoDigits = s[i-1:i+1]
        if 10 <= int(twoDigits) <= 26:
            two_prev = 1 if i == 1 else dp[i-2]
            dp[i] += two_prev

    return dp[-1]


print(decode_ways("12"))
print(decode_ways("226"))
print(decode_ways("06"))
