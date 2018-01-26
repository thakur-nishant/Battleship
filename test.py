
# def solution(A, B, M, X, Y):
#     # write your code in Python 3.6
#     i = stops = 0
#     n =len(A)
#     while n > 0:
#         w = 0
#         sfloor = []
#         for j in range(X):
#             if n > 0 and (w + A[i]) < Y:
#                 sfloor.append(B[i])
#                 w += A[i]
#                 n -= 1
#                 i += 1
#
#         print(sfloor)
#         stops += len(set(sfloor)) + 1
#
#     print(stops)
#
#
#
# # A = [60, 80, 40]
# # B = [2, 3, 5]
# x = solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200)
# # print(x)


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



                # def solution(A):
                #     # write your code in Python 3.6
                #     countryCount = 0
                #     visitedList = [[False for j in range(len(A[0]))] for i in range(len(A))]
                #     for i in range(len(A)):
                #         for j in range(len(A[0])):
                #             visitedList[i][j] = True
                #             checks = [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
                #             for check in checks:
                #                 # validity check
                #                 if check[0] >= 0 and check[1] >= 0 and check[0] < len(A) and check[1] < len(A[0]):
                #                     if A[check[0]][check[1]] == A[i][j]:
                #                         if visitedList[check[0]][check[1]]:
                #                             break
                #             countryCount += 1
                #
                #     return (countryCount + 1) // 2