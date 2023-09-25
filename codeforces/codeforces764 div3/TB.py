t = int(input())
while t > 0:
    a,b,c = map(int,input().split())
    if a + c == 2 * b:
        print("YES")
    elif a + c > 2 * b:
        print("YES") if (a + c) % 2 ==0 and ((a + c) //2) % b == 0 else print("NO")
    else:
        if (2 * b - a > c and (2 * b - a)%c == 0) or (2 *b - c > a and (2 * b - c) % a == 0):
            print("YES")
        else:
            print("NO")

    t -= 1