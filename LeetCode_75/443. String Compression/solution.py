'''
TO DO: Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:
If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.
After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Constraints:
1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
'''
class Solution:
  def compress(self, chars: List[str]) -> int:
    i = 0
    position = 0
    while i < len(chars):
      letter = chars[i]
      count_repeat = 0
      while i < len(chars) and chars[i] == letter:
        count_repeat += 1
        i += 1
      chars[position] = letter
      position += 1
      if count_repeat > 1:
        for c in str(count_repeat):
          chars[position] = c
          position += 1
    return position
