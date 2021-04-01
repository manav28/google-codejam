"""
Question:
Given a NxN matrix, compute the trace of the matrix and check whether there are any duplicate rows or columns
Such a matrix is called a latin square

Solution:
The solution is to use sets to compare duplicate elements in rows and columns
Trace can be easily computed by summing the elements in the main diagonal

Complexity:
Time: O(n^2)
Space: O(n)
"""

def get_trace(matrix):
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return trace

def get_dup_rows(matrix):
    result = 0
    for row in matrix:
        if len(row) != len(set(row)):
            result += 1
    return result

def get_dup_cols(matrix):
    result = 0
    for j in range(len(matrix)):
        col = [matrix[i][j] for i in range(len(matrix))]
        if len(col) != len(set(col)):
            result += 1
    return result
    
def vestigium(matrix):
    trace = get_trace(matrix)
    num_rows_dup = get_dup_rows(matrix)
    num_cols_dup = get_dup_cols(matrix)
    
    return trace, num_rows_dup, num_cols_dup
    
tests = int(input())
for x in range(1, tests+1):
    N = int(input())
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)
    k, r, c = vestigium(matrix)
    print("Case #{}: {} {} {}".format(x, k, r, c))