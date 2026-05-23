"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 into word2.

You have the following three operations permitted on a string:
1. Insert a character
2. Delete a character
3. Replace a character

Each operation costs 1.


Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation:
horse → rorse (replace 'h' with 'r')
rorse → rose (delete 'r')
rose → ros (delete 'e')


Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation:
intention → inention (delete 't')
inention → enention (replace 'i' with 'e')
enention → exention (replace 'n' with 'x')
exention → exection (replace 'n' with 'c')
exection → execution (insert 'u')


Constraints:
0 <= len(word1), len(word2) <= 500
word1 and word2 consist of lowercase English letters.
"""
