"""
Question:
Given a string of digits S, insert a minimum number of opening and closing parentheses into it such
that the resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Examples:
021 : 0((2)1)
312: (((3))1(2))
4: ((((4))))

Solution:
One solution is to use a greedy approach with a 2 pointer strategy and build the result in 4 phases
Lets take the example input "221"

Phase 1: Open as many '(' braces as needed from the previous number.
         The result will now be "(("
Phase 2: Append all the continuos occurences of the number.
         The result will now be "((22"
Phase 3: Start closing the left braces till it is equal to the next number in the input.
         If a later number in the loop becomes greater, open required amount of braces and repeat this process
         The result will now be "((22)1"
Phase 4: Add remaining closing braces ')'
         The result will now be "((22)1)"

This is the optimum result

Complexity:
Time: O(n)
Space: O(1)
"""
def paran(s):
    i = 0
    res = ''
    while i < len(s):
        j = i
        left = int(s[i])
        
        while j < len(s) and s[j] == s[i]:
            j += 1
        
        res += ('(' * left)
        res += s[i:j]
        
        while left and j < len(s):
            right = int(s[j])
            if right == left:
                res += s[j]
                j += 1
            elif right > left:
                res += ('(' * (right - left))
                left += (right - left)
            else:
                res += ')'
                left -= 1
                
        res += ')' * left
        i = j
    return res
    
t = int(input())
for x in range(1, t+1):
    s = input()
    result = paran(s)
    print("Case #{}: {}".format(x, result))