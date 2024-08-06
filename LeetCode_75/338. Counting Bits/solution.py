'''
TO DO: Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
'''
class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(0, n+1):
            result[i] = result[i >> 1] + (i & 1) 
            # i >> 1 - битовый сдвиг вправо на 1, это деление i // 2 и удаление младшего бита
            # result[i >> 1] - количество единичных битов(т.е. единиц в двоичном представлении) в числе после сдвига
            # i & 1 - операция "и" побитовая маска
        return result
        
