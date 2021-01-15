# Sample Input
#
# 1222311
# Sample Output
#
# (1, 1) (3, 2) (1, 3) (2, 1)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby

s = input()

print(*[(len(list(g)), int(k)) for k, g in groupby(s)], sep=" ")
