'''
TO DO: You are given an n x n integer matrix grid.
Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that: 
maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
'''
Example 1:
Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
'''
class Solution:
    def largestLocal(self, grid):
        n = len(grid)

        for i in range(1, n - 1):
            for j in range(1, n - 1):
                max_element = 0

                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        max_element = max(max_element, grid[k][l])
                grid[i - 1][j - 1] = max_element

        n = len(grid)
        grid = [row[:n-2] for row in grid[:n-2]] #Generate an integer matrix maxLocal of size (n - 2) x (n - 2)

        return grid

