class Indicium:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        self.res = [[0 for _ in range(n)] for _ in range(n)]

    def fill_diag(self):
        k = self.k
        n = self.n
        if k == n + 1 or k == (n ** 2) - 1 or not (n <= k <= n ** 2):
            return False
        elif k % n == 0:
            diag = k // n
            for i in range(self.n):
                self.res[i][i] = diag
        else:
            for i in range(1, n+1):
                first = i
                first_sum = i * (n - 2)
                r = k - first_sum
                if r > (2 * n) or r // 2 == first:
                    continue
                else:
                    second_last = r // 2
                    last = r - second_last
                    break

            for i in range(n - 2):
                self.res[i][i] = first
            
            self.res[-2][-2] = second_last
            self.res[-1][-1] = last

        return True

    def get_result(self):
        possible = self.fill_diag()
        if not possible:
            return "IMPOSSIBLE", None
        res = self.res
        res[-2][-1] = res[-1][-2] = res[0][0]

        perm = list(range(1, self.n+1))
        perm = perm[res[0][0]-1:] + perm[:res[0][0]-1]
        for i in range(n - 3):
            res[i] = perm
            perm = [perm[-1]] + perm[:-1]
        return "POSSIBLE", res

n = 6
for i in range(n, n ** 2):
    ind = Indicium(n, i)
    status, result = ind.get_result()
    print(i, status)
    if not result:
        print()
        continue
    for row in result:
        print(row)
    print()
# t = int(input())
# for x in range(1, t+1):
#     N, K = list(map(int, input().split()))
#     ind = Indicium(N, K)
#     status, result = ind.get_result()
#     print("Case #{}: {}".format(x, status))
#     if result:
#         for row in result:
#             row = list(map(str, row))
#             print(" ".join(row))