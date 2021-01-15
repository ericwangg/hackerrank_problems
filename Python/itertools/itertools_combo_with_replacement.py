# Sample Input
#
# HACK 2
# Sample Output
#
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement

if __name__ == "__main__":
    word, n = input().split(" ")

    print(*["".join(i) for i in list(combinations_with_replacement(sorted(word),int(n)))], sep="\n")
