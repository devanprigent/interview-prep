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
"""