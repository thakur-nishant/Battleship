"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order in Anti-Clockwise direction.
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []
        result = []
        hs = vs = 0
        he = len(matrix[0]) - 1
        ve = len(matrix) - 1
        while hs <= he and vs <= ve:
            for i in range(vs, ve + 1):
                result.append(matrix[i][hs])
            hs += 1

            for j in range(hs, he + 1):
                result.append(matrix[ve][j])
            ve -= 1

            if hs <= he:
                for i in range(ve, vs - 1, -1):
                    result.append(matrix[i][he])
                he -= 1
            if vs <= ve:
                for j in range(he, hs - 1, -1):
                    result.append(matrix[vs][j])
                vs += 1

        return result

