'''
TO DO: You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Example:
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"

Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        result = ""
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                result += word1[i]
            i += 1
            if j < len(word2):
                result += word2[j]
            j += 1
        return result
        
