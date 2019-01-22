import heapq
def solution(A, k):
    H = A[:k]
    heapq.heapify(H)

    for i in range(k,len(A)):
        print(H)
        if A[i] > H[0]:
            heapq.heappop(H)
            heapq.heappush(H, A[i])

    return heapq.heappop(H)



A = [2, 11, 23, 53, 34, 31]
k = 4

print(solution(A,k))
