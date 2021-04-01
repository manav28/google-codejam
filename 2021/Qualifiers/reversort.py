from itertools import permutations
def get_cost(arr):
    cost = 0
    for i in range(len(arr)-1):
        min_elem = float("inf")
        min_ix = i
        for k in range(i, len(arr)):
            if arr[k] < min_elem:
                min_elem = arr[k]
                min_ix = k
        cost += (min_ix - i + 1)
        start, end = i, min_ix
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
    return cost

def solution():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        L = list(map(int, input().split(" ")))
        print(f"Case #{t}: {get_cost(L)}")

def test():
    results = []
    for perm in permutations(range(1, 8)):
        cost = get_cost(list(perm))
        results.append(cost)
        #print(perm, cost)

    print(set(results))
