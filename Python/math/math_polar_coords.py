# Enter your code here. Read input from STDIN. Print output to STDOUT
import math, cmath

def cart_to_polar(coord):
    # print(*cmath.polar(complex(coord)), sep="\n")

    # x = cmath.polar(complex(coord))[0]
    # y = cmath.polar(complex(coord))[1]
    # print(x,y, sep="\n")

    # x = abs(complex(coord))
    # y = cmath.phase(complex(coord))
    # print(x,y, sep="\n")

    # Without using cmath
    c = coord.strip("j")
    if "+" in coord:
        i = c.find("+")
    elif coord.count("-") == 2:
        i = c[1:].find("-") + 1
    else:
        i = c.find("-")

    x = int(c[:i])
    y = int(c[i:])

    r = (x**2+y**2)**0.5
    phi = math.atan2(y,x)
    print(r,phi,sep='\n')

if __name__ == "__main__":
    cart_to_polar(input())
