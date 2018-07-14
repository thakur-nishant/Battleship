class Solution:
    def findMaxColorArea(self,matrix):
        max_area = 0
        counts = {}
        visited = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not visited[i][j]:
                    stack = [tuple([i,j])]
                    color = matrix[i][j]
                    while stack:
                        print(stack)
                        c,r = stack.pop()
                        if matrix[c][r] in counts:
                            counts[matrix[c][r]] += 1
                        else:
                            counts[matrix[c][r]] = 1
                        visited[c][r] = 1
                        if c > 0 and matrix[c][r] == matrix[c-1][r] and not visited[c-1][r]:
                            stack.append(tuple([c-1,r]))
                        if c < len(matrix) -1 and matrix[c][r] == matrix[c+1][r] and not visited[c+1][r]:
                            stack.append(tuple([c+1,r]))
                        if r > 0 and matrix[c][r] == matrix[c][r-1] and not visited[c][r-1]:
                            stack.append(tuple([c,r-1]))
                        if r < len(matrix[0]) -1 and matrix[c][r] == matrix[c][r+1] and not visited[c][r+1]:
                            stack.append(tuple([c,r+1]))

                    print(counts)
                    max_area = max(max_area,counts[color])
                    counts[color] = 0

        return max_area


matrix = [[1,3,1,3],[3,2,2,2], [1,2,3,2], [2,4,4,1]]
x = Solution().findMaxColorArea(matrix)
print(x)