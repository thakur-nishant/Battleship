def get_min_number_flights(weights):
    weights = sorted(weights)

    i = 0
    j = len(weights)-1
    max_weight = 150
    count = 0
    while i < j:
        while weights[j] > max_weight:
            print(weights[j],"discarded")
            j -= 1
            print("count:",count)

        if weights[i] > max_weight:
            return count

        if weights[i] + weights[j] <= max_weight:
            count += 1
            print(weights[i], weights[j])

            i += 1
            j -= 1
            print("count:",count)

        elif weights[j] <= max_weight:
            print(weights[j])
            count += 1
            j -= 1
            print("count:",count)

        else:
            print(weights[i])
            count += 1
            i += 1
            print("count:",count)

        if i == j:
            print(weights[i])
            count += 1
            print("count:",count)

    return count

w = [25,45,47,75,97,149]
# w = [9,126,127,10,1,129,125,123,124,3,120,121,8,5,7,128,122,4,6,2]
x = get_min_number_flights(w)
print(x)

