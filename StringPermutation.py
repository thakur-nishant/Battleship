def string_permutation(s):
    """
    :param s: String
    :return: [List[List]]
    """
    s = sorted(s)
    result = []
    for i in range(len(s)):
        helper([s[i]] , s[:i]+s[i+1:], result)

    return result


def helper(pre ,s, result):
    """
    :param s: String
    :param result: [List[List]]
    :return: None
    """
    key = ''.join(pre)
    if key in result:
        return

    if not s:
        result.append(key)
        return

    for i in range(len(s)):
        helper(pre+[s[i]], s[:i] + s[i + 1:], result)


s = "AABC"
test = string_permutation(s)
print(len(test),test)
