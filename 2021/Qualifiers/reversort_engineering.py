def get_solution(N, cost):
    if not (N - 1 <= cost <= (N * (N+1) // 2) - 1):
        return "IMPOSSIBLE"
    
    result = [0] * N
    elems_rem = N - 1
    curr_elem = sign = 1
    left, right = 0, N - 1
    curr_ix = 0

    while cost > elems_rem:
        choice = min(elems_rem+1, cost-elems_rem+1)
        if sign == 1:
            curr_ix = left+choice-1
            result[curr_ix] = curr_elem
            right -= 1
        else:
            curr_ix = right-choice+1
            result[curr_ix] = curr_elem
            left += 1
        cost -= choice
        elems_rem -= 1
        curr_elem += 1
        sign *= -1
    
    def progress_left(curr_ix, curr_elem):
        i = curr_ix
        while i >= 0:
            if result[i] == 0:
                result[i] = curr_elem
                curr_elem += 1
            i -= 1
        return curr_elem
    
    def progress_right(curr_ix, curr_elem):
        i = curr_ix
        while i < N:
            if result[i] == 0:
                result[i] = curr_elem
                curr_elem += 1
            i += 1
        return curr_elem

    if sign == 1:
        curr_elem = progress_right(curr_ix, curr_elem)
        curr_elem = progress_left(curr_ix, curr_elem)
    else:
        curr_elem = progress_left(curr_ix, curr_elem)
        curr_elem = progress_right(curr_ix, curr_elem)
    
    return ' '.join(map(str, result))

T = int(input())
for t in range(1, T+1):
    N, cost = map(int, input().split(" "))
    result = get_solution(N, cost)
    print(f"Case #{t}: {result}")
