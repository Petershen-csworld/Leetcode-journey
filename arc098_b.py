from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
###统计元素和 == 元素异或和
###1.暴力枚举 O（n^1）
###2.pre[j+1]-pre[i] == xor[j+1] ^ xor[i]
### pre[j + 1] = (xor[j + 1] ^ xor[i]) + pre[i]
### pre[j + 1] ^ x
