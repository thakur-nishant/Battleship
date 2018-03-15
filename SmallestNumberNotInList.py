def solution(nums):
    record = {}

    for num in nums:
        record[num] = 1

    i = 1
    while True:
        if i in record:
            i += 1
        else:
            return i


nums = [1,2,3,4,6,7,8]
x = solution(nums)

print(x)
