"""
Give an positive integer n, find out the smallest integer m, such that all digits in m multiply equals to n.
For example, n = 36, return 49. n = 72, return 89. You can assume there is no overflow.
"""

def mult_num(num):
    result = 1
    for i in num:
        result *= int(i)

    return result

def min_num_combination(num):
    l = sorted(list(str(num)))
    result = ""
    for i in l:
        result += i
    return int(result)

def solution(n):
    result = int(str(n) + '1')

    for i in range(1,n+1):
        if n%i == 0:
            num = str(i)
            num += str(n//i)

            if n == mult_num(num):
                res = min_num_combination(num)
                result = min(result, res)

    return  result


n = 60
x = solution(n)
print(x)

