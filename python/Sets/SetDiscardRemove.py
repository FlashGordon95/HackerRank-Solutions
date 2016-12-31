"""
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer , the number of elements in the set .
The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer , the number of commands.
The next  lines contains either pop, remove and/or discard commands followed by their associated value.
"""


n = int(input())
s = set(map(int, input().split()))
m = int(input())

for i in range(m):
    eval('s.{0}({1})'.format(*input().split() + ['']))

print(sum(s))