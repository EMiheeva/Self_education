'''
TO DO: Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Constraints:
1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
#My solution: time 265 ms, memory 19.00 mb
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        letter_in_vowels = []
        position_letter = []
        for i in range(len(s)):
            if s[i] in vowels:
                letter_in_vowels.append(s[i])
                position_letter.append(i)
        for j in range(len(position_letter)):
            s = s[:position_letter[j]] + letter_in_vowels[-j-1] + s[position_letter[j]+1:]
        return s
#time 46 ms
class SolutionBest:
    def reverseVowels(self, s: str) -> str:
        s = list(s)  # Convert the string to a list (since strings are immutable)
        l, r = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        while l < r:
            if s[l] in vowels and s[r] in vowels:
                # Swap vowels
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels:
                r -= 1
            else:
                l += 1
        return "".join(s) # Convert the list back to a string

