t = int(input())
while t > 0:
    s = input()
    if s == "abc" or s == "acb" or  s == "cba" or s == "bac":
        print("YES")
    else:
        print("NO")
    t -= 1