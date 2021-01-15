# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
# For Example:
#
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2
# Input Format
#
# A single line containing a string .
#
# Constraints
#
#
# Output Format
#
# Print the modified string .
#
# Sample Input 0
#
# HackerRank.com presents "Pythonist 2".
# Sample Output 0
#
# hACKERrANK.COM PRESENTS "pYTHONIST 2".

def swap_case(s):
    return ''.join(char.upper() if char.islower() else char.lower() for char in s)

    # return s.swapcase()

    # swap = ""
    # for c in s:
    #     if c.islower():
    #         swap += c.upper()
    #     else:
    #         swap += c.lower()
    # return swap

    # swap = []
    # for i in list(s):
    #     if i.islower():
    #         swap.append(i.upper())
    #     else:
    #         swap.append(i.lower())
    # return ''.join(swap)

    # swap = list(s)
    # for i,j in enumerate(swap):
    #     if swap[i].islower():
    #         swap[i] = swap[i].upper()
    #     else:
    #         swap[i] = swap[i].lower()
    # return ''.join(swap)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
