if __name__ == '__main__':
    n = int(raw_input())

    if (n % 2 == 1):
        print("Weird")
        print("Condition 1")
    elif (n % 2 == 0 & n in range(2, 6)):
        print("Not Weird")
    elif (n % 2 == 0 & n in range(6, 21)):
        print("Weird")
    elif (n > 20 & n % 2 == 0):
        print("Not Weird")