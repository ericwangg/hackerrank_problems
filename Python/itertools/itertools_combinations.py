# Sample Input
#
# HACK 2
# Sample Output
#
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == "__main__":
    word, n = input().split(" ")
    print(*["".join(j) for i in range(1, int(n)+1) for j in list(combinations(sorted(word), i)) ], sep="\n")
