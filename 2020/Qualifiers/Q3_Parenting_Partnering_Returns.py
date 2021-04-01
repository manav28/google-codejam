"""
Question:
Cameron and Jamie have a list of N activities to take care of during the day. 
Each activity happens during a specified interval during the day. 
They need to assign each activity to one of them, so that neither of them is responsible for 
two activities that overlap. An activity that ends at time t is not considered to overlap with another activity that starts at time t.

Given the starting and ending times of each activity, find any schedule that does not 
require the same person to cover overlapping activities, or say that it is impossible.

Use 'C' for Cameron and 'J' for Jamie

Example:
Imput:
3
360 480
420 540
600 660

Output:
CJC

Solution:
A greedy approcah is appropriate.

Sort the schedule by starting time, keep track of the 
ending time of the current tasks assigned to both
and assign the task to whoever is available.

If both of them have tasks at hand while a new task begins, the schedule would be impossible

Note: The result needs to have the same order as the initial schedule. 
      So we need to sort the result by the index of the original schedule

Complexity:
Time: O(nlgn)
Space: O(n)
"""
def get_schedule(sched):
    if not sched:
        return ''
    occ = {'C':0, 'J':0}
    res = []
    sched_copy = sorted(sched, key=lambda x: x[0])
    for interval in sched_copy:
        if occ['C'] <= interval[0]:
            res.append(('C', interval[2]))
            occ['C'] = interval[1]
        elif occ['J'] <= interval[0]:
            res.append(('J', interval[2]))
            occ['J'] = interval[1]
        else:
            return "IMPOSSIBLE"
    res.sort(key=lambda x: x[1])
    return ''.join([x[0] for x in res])

t = int(input())
for x in range(1, t+1):
    N = int(input())
    sched = []
    for i in range(N):
        time = list(map(int, input().split())) + [i]
        sched.append(time)
    result = get_schedule(sched)
    print("Case #{}: {}".format(x, result))