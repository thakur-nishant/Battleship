# def solution(A):
#     # write your code in Python 3.6
#     visited = [[False for j in range(len(A[0]))] for i in range(len(A))]
#     count = 0
#     for i in range(len(A)):
#         for j in range(len(A[0])):
#             if not visited[i][j]:
#                 visited[i][j] = True
#                 east = west = north = south = True
#                 if j-1 >= 0 and A[i][j] == A[i][j - 1]:
#                     if visited[i][j - 1]:
#                         west = False
#
#                 if i-1 >= 0 and A[i][j] == A[i - 1][j]:
#                     if visited[i - 1][j]:
#                         north = False
#
#                 if j+1 < len(A[0]) and A[i][j] == A[i][j+1]:
#                     if visited[i][j+1]:
#                         east = False
#                     visited[i][j+1] = True
#
#                 if i+1 < len(A) and A[i][j] == A[i+1][j]:
#                     if visited[i+1][j]:
#                         east = False
#                     visited[i+1][j] = True
#
#                 if west and north and east and south:
#                     count += 1
#     return count

def solution(A):
    visited = [[0 for i in range(len(A[0]))] for i in range(len(A))]
    count = 0

    for i in range(len(A)):
        for j in range(len(A[0])):
            if not visited[i][j]:
                count += 1
                stack = [[i,j]]
                while stack:
                    c,r = stack.pop()
                    visited[c][r] = 1

                    if c > 0 and A[c][r] == A[c-1][r] and not visited[c-1][r]:
                        stack.append([c-1, r])
                    if c < len(A) - 1 and A[c][r] == A[c+1][r] and not visited[c+1][r]:
                        stack.append([c+1,r])
                    if r > 0 and A[c][r] == A[c][r-1] and not visited[c][r-1]:
                        stack.append([c,r-1])
                    if r < len(A[0]) - 1 and A[c][r] == A[c][r+1] and not visited[c][r+1]:
                        stack.append([c,r+1])

    return count


A = [
    [5,4,4], [4,3,4], [3,2,4], [2,2,2], [3,3,4], [1,4,4], [4,1,1]
]
print(solution(A))