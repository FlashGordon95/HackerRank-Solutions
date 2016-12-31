"""



"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
s = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))

print(len(s^b))