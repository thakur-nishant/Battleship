"""
Given a string, generate all possible subsequence of a given length
"""

def subsequenceOfLengthK(S, K):
    n = len(S)
    result = []
    for counter in range(1, 1 << n):
        curr_list = []
        for j in range(n):
            # Check if jth bit in the counter is set.
            # If set then print jth element from S.
            if counter & 1 << j:
                curr_list.append(S[j])
        # if len(curr_list) == K:
        #     result.append(curr_list)
        result.append(curr_list)

    return result


print(subsequenceOfLengthK('abcd', 3))


