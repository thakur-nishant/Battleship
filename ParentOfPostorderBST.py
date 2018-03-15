def getParent(node, size):
    rank = index = size
    while (rank > 0):

        leftIndex = index - (rank + 1)//2
        rightIndex = index - 1

        if (node == leftIndex or node == rightIndex):
            return index

        index = (leftIndex if node < leftIndex else rightIndex)
        rank  = (rank - 1)//2


def generate_answer():
    # height = int(sys.stdin.readline().strip())
    height = 3
    # p = [int(num) for num in sys.stdin.readline().strip().split()]
    p = [3,5,7,1]
    q = []
    for num in p:
        parent = getParent(num, (2**height)-1)
        if parent:
            q.append(parent)
        else:
            q.append(-1)

    #   q = [1, 2, 3]
    print (" ".join([str(num) for num in q]))



generate_answer()

