"""
Given a string s and a list of words (dictionary),
return True if s can be fully segmented into one or
more words from the dictionary, False otherwise.

Example 1:
s = "leetcode", words = ["leet", "code"]
→ Output: True  # "leet" + "code"

Example 2:
s = "applepenapple", words = ["apple", "pen"]
→ Output: True  # "apple" + "pen" + "apple"

Example 3:
s = "catsandog", words = ["cats", "dog", "sand", "and", "cat"]
→ Output: False
"""

# The first natural approach is a greedy algorithm.
# I.e. to maintain a cursor that goes through the string
# and tries to identify the longest word that can be done
# with the characters seen so far.
# But if you try to do it mentally with the third example,
# you'll realize that's the wrong approach. The issue is
# when you have overlapping prefixes like cat and cats.
# With that kind of input, the greedy algorithm will have
# to make a decision : either to always choose the first word
# (cat here) or most probably the longest one (cats here).
# Because of that, the input
# s = "catsanddog", words = ["cats", "dog", "sand", "and", "cat"]
# would return False whereas it can be fully segmented "cat" "sand" "dog".
# So a greedy algorithm is not a good approach. We need an algorithm
# that doesn't go letter by letter but instead, consider all possibilities
# depending on where you slice the string.

# Because we need all possibilities, the next approach is to try a bruteforce.
# The idea would be to consider all possible prefixes p of s,
# check if this prefix is in the dictionnary
# check if the rest can be broken down
# It would look like this:

# def canBeBrokeDown(s):
#   if length(s) == 0: return True
#   for prefix p in s:
#       is p in dict and canBeBrokeDown(rest(s)):
#           return True
#   return False


# It works but the time complexity is exponential.
# However, if we look closely, we are doing many calculations several times.
# Which means that if we find a way to memorize those calculations instead
# of redoing them, we could improve the complexity.

# We have a working solution with overlapping subproblems ->
# that leads us to a dp approach.
# The idea is to keep an array dp where
# dp[i] is the answer to the question: is the substring s[:i] segmentable ?


def word_break(s: str, words: list[str]):
    n = len(s)
    possibilities = set(words)
    dp = [True] + [False]*n

    for i in range(1, n+1):
        for j in range(i):
            if dp[j] and s[j:i] in possibilities:
                dp[i] = True
                break
    return dp[-1]


s = "leetcode"
words = ["leet", "code"]
print(word_break(s, words))

s = "applepenapple"
words = ["apple", "pen"]
print(word_break(s, words))

s = "catsandog"
words = ["cats", "dog", "sand", "and", "cat"]
print(word_break(s, words))

"""
MANUAL EXECUTION
word_break("leetcode", ["leet", "code"])

dp = [True, False, False, False, False, False, False, False, False]
i=1
j=0
dp[j]=True and s[0:1] in possibilites = False

...
i=4
j=0
dp[j]=True and s[0:4] in possibilites = True -> dp[4] = True

i = 8
    j=0
    dp[0] = True and s[0:8] in possibilities = False
    ...
    j=4
    dp[4] = True and s[4:8]="code" in possibilities = True
    dp[8] = True

dp = [True, False, False, False, True, False, False, False, True]

"""
