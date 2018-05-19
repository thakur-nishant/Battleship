# Program to reduce the string with same adjacent characters recursively

def reduce_string(s):
    result = ''
    i = 1
    while i < len(s):
        if s[i] == s[i-1]:
            i += 2
        else:
            result+=s[i-1]
            i += 1

    if i == len(s):
        result+=s[i-1]

    if result == s:
        return s
    if result:
        result = reduce_string(result)
    else:
        result = 'Empty String'
    return result



s = "abbacc"
x = reduce_string(s)
print(x)
