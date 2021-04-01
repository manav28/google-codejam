"""def get_answer(n):
    if n <= 30:
        for row in range(1, n+1):
            print(row, 1)
        return
    n -= 30
    left = True
    row = 1
    end = 30
    while n:
        if n & 1:
            if left:
                for col in range(1, row+1):
                    print(row, col)
            else:
                for col in range(row, 0, -1):
                    print(row, col)
            left ^= True
        else:
            end -= 1
            if left:
                print(row, 1)
            else:
                print(row, row)
        n >>= 1
        row += 1
    for r in range(row, row+end):
        if left:
            print(r, 1)
        else:
            print(r, r)
    
tests = int(input())
for x in range(1, tests+1):
    N = int(input())
    print("Case #{}:".format(x))
    get_answer(N)"""
#python 3.5.2
"""import heapq

#
# @param Integer src
# @param Integer dest
# @param Array[][] wizards
# @return Array[Integer, Array[]] [Min Cost, Array Min Path]
#

def getMinMagic(src, dst, wizards):
        minCost = float("inf")
        minPath = []
        # Put your code here to calculate minCost and minPath
        def get_weight(a, b):
            return (a - b) ** 2
        shortest_distance = {i:float("inf") for i in range(len(wizards))}
        shortest_distance[src] = 0
        unseen_nodes = {i:wizards[i] for i in range(len(wizards))}
        predecessor = {}

        while unseen_nodes:
            min_node = None
            for node in unseen_nodes:
                if min_node is None:
                    min_node = node
                elif shortest_distance[node] < shortest_distance[min_node]:
                    min_node = node
            
            for child in wizards[min_node]:
                weight = get_weight(child, min_node)
                if weight + shortest_distance[min_node] < shortest_distance[child]:
                    shortest_distance[child] = weight + shortest_distance[min_node]
                    predecessor[child] = min_node
            unseen_nodes.pop(min_node)

        if shortest_distance[dst] == float("inf"):
            return minCost, minPath

        minCost = shortest_distance[dst]
        curr_node = dst
        while curr_node != src:
            try:
                minPath.append(curr_node)
                curr_node = predecessor[curr_node]
            except KeyError:
                print("Path not reachable")
                break
        minPath.append(src)
        minPath.reverse()
        # Return the result, do not change the structure
        return minCost, minPath
    
def get_matrix():
    row = 10
    grid = [[] for y in range(row)]

    for i in range(row):
        line = input()
        grid[i] = [int(x) for x in list(line)]
    return grid

#if __name__ == "__main__":
    
src = int(input())
dest = int(input())
matrix = get_matrix()
minCost, minPath = getMinMagic(src, dest, matrix)
result = str(minCost) + " " + "".join([str(elem) for elem in minPath]) 
print(result)"""



"""def get_answer(arr):
    
tests = int(input())
for x in range(1, tests+1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = get_answer(arr)
    print("Case #{}: {}".format(x, ans))
"""

def get_square(s):
    res = [1, 1]
    def check(ch):
        if ch == 'N':
            if res[1] == 1:
                res[1] = 10 ** 9
            else:
                res[1] -= 1
        
        elif ch == 'S':
            if res[1] == 10 ** 9:
                res[1] = 1
            else:
                res[1] += 1
        
        elif ch == 'W':
            if res[0] == 1:
                res[0] == 10 ** 9
            else:
                res[0] -= 1
        else:
            if res[0] == 10 ** 9:
                res[0] = 1
            else:
                res[0] += 1
    def build_string(i, reps, temp, open_braces):
        if i == len(s):
            return i, temp
        elif s[i] == ')':
            if open_braces == 0:
                return i, temp * reps
            else:
                j, t = build_string(i+1, reps, temp, open_braces-1)
                t = temp + t
                return j, t
        elif s[i].isnumeric():
            j, t = build_string(i+2, int(s[i]), "", open_braces+1)
            t = temp + t
            t *= reps
            return j, t
        else:
            j, t = build_string(i+1, reps, temp + s[i], open_braces)
            return j, t
    i = 0
    while i < len(s):
        ch = s[i]
        if ch.isnumeric():
            i, temp = build_string(i, 1, "", 0)
            print(temp)
            for ch in temp:
                check(ch)
            continue
        else:
            check(ch)
            i += 1   
    return res

tests = int(input())
for x in range(1, tests+1):
    s = input()
    ans = get_square(s)
    print("Case #{}: {} {}".format(x, *ans))