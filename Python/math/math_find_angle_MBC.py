

Sample Input

10
10
Sample Output

45°

# Notes: Since splitting ABC into 2 triangles at M produces 2 isosceles triangles, calculating angle MBC = angle MCB
# angle MCB can be calculated using cos^-1(BC/Hypotenuse)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

if __name__ == "__main__":
    AB, BC = (int(input()) for _ in range(2))
    hyp = math.hypot(AB,BC)
    ang = round(math.degrees(math.acos(BC/hyp)))
    deg = chr(176)
    print(ang,deg,sep="")
