def get_cost(X, Y, S):
    cost = i = 0
    
    while i < len(S) and S[i] == '?':
        i += 1

    stack = [S[i]] if i < len(S) else []
    i += 1

    while i < len(S):
        if S[i] == 'C':
            if stack[-1] == 'J':
                cost += Y
            stack.append('C')
        elif S[i] == 'J':
            if stack[-1] == 'C':
                cost += X
            stack.append('J')
        else:
            if i < len(S) - 1:
                if stack[-1] == 'C' and S[i+1] == 'J':
                    cost += X
                    stack.append('J')
                elif stack[-1] == 'J' and S[i+1] == 'C':
                    cost += Y
                    stack.append('C')
                else:
                    stack.append(stack[-1])
        i += 1

    return cost

T = int(input())
for t in range(1, T+1):
    X, Y, S = input().split(" ")
    X, Y = int(X), int(Y)
    print(f"Case #{t}: {get_cost(X, Y, S)}")
