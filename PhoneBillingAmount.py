import math

def solution(S):
    S = S.split()
    records = {}

    for rec in S:
        rec = rec.split(',')
        number = rec[1]
        t = rec[0].split(':')
        sec = (int(t[0])*60*60) + (int(t[1])*60) + int(t[2])
        if number in records:
            records[number] += sec
        else:
            records[number] = sec

    free = max(records, key=records.get)

    del records[free]
    amount = 0
    print(records)
    for key  in records:
        if records[key] >= 300:
            amount += math.ceil(records[key]/60) * 150
        else:
            amount += records[key] * 3

    print(amount)


S = """00:01:07,400-234-090
   00:05:01,701-080-080
   00:05:00,400-234-090
   00:01:07,400-234-080
   00:05:00,400-234-080"""
solution(S)