# Sample Input
#
# 177
# 10
# Sample Output
#
# 17
# 7
# (17, 7)

# Enter your code here. Read input from STDIN. Print output to STDOUT
def my_divmod(a, b):
    q = a//b
    r = a % b
    print(q, r, (q, r), sep="\n")

if __name__ == "__main__":
    a,b = (int(input()) for _ in range(2))
    # print("{d[0]}\n{d[1]}\n({d[0]}, {d[1]})".format(d=divmod(a,b)))
    my_divmod(a,b)
