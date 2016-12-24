"""
Input Format

The first line contains the integer, , the total number of plants.
The second line contains the  space separated heights of the plants.

Constraints
We only want the average of distinct values
If we see a second number of same value this is not regarded in the sum or length of the set


Output Format

Output the average height value on a single line.

"""
def average(array):
    # your code goes here
    s = set(array) # Cast the array into a set. This will take care of the distinct values
    return sum(s) / len(s) # Same calculation we would do on the array only after casting will give a different value


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)