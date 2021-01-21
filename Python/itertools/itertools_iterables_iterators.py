# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.
#
# To read more about the functions in this module, check out their documentation here.
#
# You are given a list of N lowercase English letters. For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
#
# Find the probability that at least one of the K indices selected will contain the letter: 'a'.

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Sample Input
#
# 4
# a a c d
# 2
# Sample Output
#
# 0.8333

from itertools import combinations

def iter_prob(N,L,K):
    c = list(combinations(L,K))
    f = list(filter(lambda c : 'a' in c, c))
    print(len(f)/len(c))

    # #generates p combinations of numbers for c combinations of 1 to N, used to check if these indicies match with the indices of 'a' in L
    # not nearly as efficient as taking combos of L, just the string list itself, and filtering out the ones that have 'a's inside the tupels
    # p = [i for i in range(1,N+1)]
    # c = list(combinations(p,K))
    # combos = len(c)
    # num = 0
    # a_index = [i+1 for i,j in enumerate(L) if j == 'a' ]
    # for i in c:
    #     if any(n in i for n in a_index):
    #         num += 1
    # print(num/combos)

if __name__ == "__main__":
    N = int(input())
    L = input().split()
    K = int(input())
    iter_prob(N,L,K)
