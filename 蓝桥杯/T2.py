import os
import sys

n,q = map(int,input().split())
for i in range(q):
   s = input()
   begin = 1
   l = 1
   for ch in s:
     if ch == "R":
       begin = (begin<<1) + 1
     else:
       begin <<= 1
     l <<= 1
   print(begin - l + 1)