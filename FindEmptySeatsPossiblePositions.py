
def solution(N, S):
    # write your code in Python 3.6
    column = "ABCDEFGHJK"
    count = 0

    S = S.split()
    occupied = {}
    for seat in S:
        col_index = column.index(seat[-1])
        row_index = int(seat[:-1]) - 1
        if row_index in occupied:
            occupied[row_index].append(col_index)
        else:
            occupied[row_index] = [col_index]

    for row in range(N):
        col = [0] * len(column)
        if row in occupied:
            for reserved in occupied[row]:
                col[reserved] = 1

        if sum(col[0:3]) == 0:
            count += 1
        if sum(col[3:6]) == 0 or sum(col[4:7]) == 0:
            count += 1
        if sum(col[7:10]) == 0:
            count += 1

    return count

N = 4
S = "1A 4F 2J 2B"
x = solution(N,S)
print(x)
