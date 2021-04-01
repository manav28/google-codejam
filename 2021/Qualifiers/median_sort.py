import random

def query(a, b, c):
    pairs = [(hidden.index(val), val) for val in (a, b, c)]
    return sorted(pairs)[1][1]

def merge(A, B):
    pass

def find_endpoints(ixset):
    while len(ixset) > 2:
        a, b, c = (ixset.pop() for _ in range(3))
        median = query(a, b, c)
        for elem in (a, b, c):
            if elem != median:
                ixset.add(elem)

    assert len(ixset) == 2
    return tuple(ixset)

def solve():
    for _ in range(T):
        items = set(range(1, N+1))
        if N % 3 != 0:
            e1, e2 = find_endpoints(items.copy())
        else:
            e1 = e2 = None
        print(e1, e2)
        if N % 3 == 1:
            items.remove(e1)
        elif N % 3 == 2:
            items.remove(e1)
            items.remove(e2)

T, N, Q = map(int, input().split(" "))
hidden = list(range(1, N+1))
random.shuffle(hidden)
print(hidden)
solve()