n = input()
ans = True
for i in range(len(n) - 1):
    if int(n[i]) <= int(n[i + 1]):
        ans = False

print("Yes") if ans else print("No")