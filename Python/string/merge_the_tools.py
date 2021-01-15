# Sample Input
#
# STDIN       Function
# -----       --------
# AABCAAADA   s = 'AABCAAADA'
# 3           k = 3
# Sample Output
#
# AB
# CA
# AD
#
# Explanation
# Split s into n\k = 9\3 = 3 equal parts of length k = 3. Convert each t_i to u_i by removing any subsequent occurrences of non-distinct characters in t_i:
#
# print each u_i on a new line


def merge_the_tools(string, k):
    # your code goes here
    # substrings = [string[i:i+k] for i in range(0, len(string),k)]

    # t = []
    # for substring in substrings:
    #     temp = ""
    #     for j in substring:
    #         if j not in temp:
    #             temp += j
    #     t.append(temp)

    # print('\n'.join(t))

    for i in range(0,len(string),k):
        sub=string[i:i+k]
        print("".join(dict.fromkeys(sub)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
