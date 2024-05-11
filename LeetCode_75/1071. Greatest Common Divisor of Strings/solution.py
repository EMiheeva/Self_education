'''
TO DO: For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
'''
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return "" #gcd not exsits
        if len(str1) == len(str2):
            return str1 #If the lengths of str1 and str2 are equal, and the concatenated strings are equal, then str1 itself is the gcd
        if len(str1) > len(str2):
            return self.gcdOfStrings(str1[len(str2):], str2) #it means that str1 contains str2 as a prefix => we recurse with the substring of str1 after slicing the prefix that matches str2.
        return self.gcdOfStrings(str1, str2[len(str1):]) #else 
