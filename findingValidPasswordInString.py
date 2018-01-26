"""
Password should contain at least one Uppercase character(A-Z) and should not contain any numbers(0-9).
Given a string S find a longest valid password from the string.

eg. S = "a0Ba"
    so return 2 as "Ba" is a valid password.
"""
def solution(S):
    # write your code in Python 3.6
    passList = []
    start = end = 0
    for i in range(len(S)):
        if S[i].isdigit():
            passList.append(S[start:end])
            start = end = i + 1
        else:
            end += 1
    passList.append(S[start:end])

    result = -1
    for str in passList:
        isUp = False
        for x in str:
            if x.isupper():
                isUp = True
        if isUp:
            result = max(result, len(str))

    return result



S = "abc909Csd2dww"
print(solution(S))