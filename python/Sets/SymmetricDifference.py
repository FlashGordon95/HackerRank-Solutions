"""
Task
Given  sets of integers, m and n, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist in either  or  but do not exist in both.


"""




# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
ls = [int(x) for x in input().split()]
s1 = set(ls)

n = int(input())
ls = [int(x) for x in input().split()]
s2 = set(ls)

ls = [x for x in s1.difference(s2)]
ls.extend([x for x in s2.difference(s1)])
ls.sort()

for x in ls:
    print(x)