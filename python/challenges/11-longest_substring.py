"""
Given a string s, find the length of the longest substring
that contains no repeating characters.
"""

def lengthOfLongestSubstring(self, s: str) -> int:
    # Let's try a brute-force solution
    if not s:
        return 0
    n = len(s)
    max_sub = 1
    for i in range(1, n):
        curr_long_sub = s[i]
        for j in range(i-1, -1, -1):
            if s[j] not in curr_long_sub:
                curr_long_sub = s[j: i+1]
                max_sub = max(max_sub, len(curr_long_sub))
            else:
                break
    return max_sub


"""
"abcabcbb"
n = 8
max_long_sub = "a"
i=1
    curr_long_sub = "b"
    j=0
    if "a" not in "b":
        curr_long_sub = s[0:2] = "ab"
        max_long_sub = 2
i=2
    curr_long_sub = "c"
    j=1
    if "b" not in "c":
        curr_long_sub = "bc"
    j=0
    if "a" not in "bc":
        curr_long_sub = "abc"
        max_long_sub = 3

It works !
But the space complexity is O(n)
and the time complexity is O(n**3)
We can improve this
First optimization is to try to get read of the two operations inside the nested loop that creates the O(n**3):
    - the membership scan
    - the slice
"""


def lengthOfLongestSubstringQuadratic(self, s: str) -> int:
    if not s:
        return 0
    n = len(s)
    max_sub = 1
    for i in range(1, n):
        curr_sub = 1
        seen = set(s[i])
        for j in range(i-1, -1, -1):
            if s[j] not in seen:
                curr_sub += 1
                seen.add(s[j])
                max_sub = max(max_sub, curr_sub)
            else:
                break
    return max_sub


"""
It works and now the complexity is:
- O(n) for space complexity
- O(n**2) for time complexity

It's much faster.

But we can do ever better because there are overlapping computations.

"""


def lengthOfLongestSubstringOptimal(self, s: str) -> int:
    if not s:
        return 0
    n = len(s)
    max_sub = 1
    start = 0
    seen = set(s[0])

    for i in range(1, n):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[i])
        max_sub = max(max_sub, (i+1)-start)

    return max_sub

"""
What's the time complexity ?

The for loop goes through the entire string: O(n).

What about the while loop?

The while loop removes an element from the seen SET. Each character is
added to the set exactly once and removed at most once. So the while
body runs at most n times across the ENTIRE run of the function — not
n times per outer iteration. That's the amortized argument.

Total work: n (for loop) + n (all while iterations combined) = 2n -> O(n).

Space: O(n), bounded by the alphabet size, for the set.

Time complexity is linear.

"""