def solution(A, B, M, X, Y):
    # write your code in Python 3.6
    i = stops = 0
    n =len(A)
    while n > 0:
        w = 0
        sfloor = []
        for j in range(X):
            if n > 0 and (w + A[i]) < Y:
                sfloor.append(B[i])
                w += A[i]
                n -= 1
                i += 1

        print(sfloor)
        stops += len(set(sfloor)) + 1

    print(stops)



# A = [60, 80, 40]
# B = [2, 3, 5]
x = solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200)
# print(x)
