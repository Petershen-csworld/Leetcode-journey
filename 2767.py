def check(v):
            cur = 0
            for i in range(len(v) - 1, -1, -1):
                cur += int(v[i]) << (len(v) - i - 1)
            while cur % 5 == 0:
                cur //= 5
            return cur == 1
print(check("10"))

