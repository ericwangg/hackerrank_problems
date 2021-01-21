# Sample Input
#
# 08 05 2015
# Sample Output
#
# WEDNESDAY

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

def calendar_date(M,D,Y):
    print(calendar.day_name[calendar.weekday(Y,M,D)].upper())

if __name__ == "__main__":
    M, D, Y = map(int, input().split())
    calendar_date(M,D,Y)
