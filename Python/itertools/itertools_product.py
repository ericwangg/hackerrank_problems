# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

# Output the space separated tuples of the cartesian product.
#
# Sample Input
#
#  1 2
#  3 4
# Sample Output
#
#  (1, 3) (1, 4) (2, 3) (2, 4)

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == "__main__":
    A = map(int, input().split())
    B = map(int, input().split())
    print(*(product(A,B)))
