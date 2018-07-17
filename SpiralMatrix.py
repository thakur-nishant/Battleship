"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        hor = len(matrix[0])
        ver = len(matrix) - 1
        i, j = 0, 0
        res = []
        while hor > 0 or ver > 0:
            # go right
            steps = hor
            while steps > 0 and ver >= 0 and hor >= 0:
                res.append(matrix[i][j])
                j += 1
                steps -= 1
            j -= 1
            print(i,j,res, hor, ver)
            # go down
            i += 1
            hor -= 1
            steps = ver
            while steps > 0 and hor >= 0 and ver >= 0:
                res.append(matrix[i][j])
                i += 1
                steps -= 1
            i -= 1
            print(i,j,res, hor, ver)
            # go left
            j -= 1
            ver -= 1
            steps = hor
            while steps > 0 and ver >= 0 and hor >= 0:
                res.append(matrix[i][j])
                j -= 1
                steps -= 1
            j += 1
            print(i,j,res, hor, ver)
            # go up
            i -= 1
            hor -= 1
            steps = ver
            while steps > 0 and ver >= 0 and hor >= 0:
                res.append(matrix[i][j])
                i -= 1
                steps -= 1
            i += 1
            print(i,j,res, hor, ver)
            j += 1
            ver -= 1

        return res


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]
x = Solution().spiralOrder(matrix)
print(x)
