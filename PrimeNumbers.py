import math
for n in range(2,30):
    l = math.floor(math.sqrt(n))

    for i in range(2,l+1):
        if n%i == 0:
                # print(n, "is not a prime number")
                # print(n, "=", n/i,"/",i)
                break
    else:
        # print(n, "is a prime number")
        print(n)
        