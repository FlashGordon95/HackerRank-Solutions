def is_leap(year):
    # Write your logic here
    if (year % 4 == 0 & year % 100 ==0 & year %400):
        leap = True
    else:
        leap = False

    return leap



year = int(raw_input())
print is_leap(year)