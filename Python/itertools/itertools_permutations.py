# Sample Input
#
# HACK 2
# Sample Output
#
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

if __name__ == "__main__":
    word, n = input().split(" ")
    print(*[''.join(i) for i in list(permutations(sorted(word), int(n)))], sep='\n' )
