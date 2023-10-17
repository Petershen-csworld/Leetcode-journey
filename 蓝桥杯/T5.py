import os
import sys

# 请在此输入您的代码
n = int(input())
s = input()
t = input()
sec = ""
for i in range(n):
    if t[i].islower():
        sec += t[i].upper()
    else:
        sec += t[i].lower()
s = s + s

def get_next():
    next = [0 for _ in range(n)]
    j = 0
    for _ in range(1,n):
        while j > 0 and sec[j] != sec[next[j]]:
            j = next[j - 1]
        if sec[j] == sec[next[j]]:
            j += 1
        next[_] = j
    return next


kmp = get_next()
j = 0
found = False
res = 0
for i in range(2*n - 1):
    while j > 0 and s[i] != sec[j]:
        j = kmp[j - 1]
    if s[i] == sec[j]:
        j += 1
        res = i - n + 1
    if j == n:
        found = True
        break
if found:
    print("Yes")
    print(res)
else:
    print("No")