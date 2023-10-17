t = int(input())
while t > 0:
    s = input()
    ## enumerate the substring ?
    ## binary search
    n = len(s)
    out1 = s.count("1")

    ### 二分代价
    def check(cost):
        j = 0
        zero = 0
        one = 0
        for i in range(n):
            if s[i] == "0":
                zero += 1
            else:
                one += 1
            while j < i and zero > cost:
                val = s[j]
                if val == "0":
                    zero -= 1
                else:
                    one -= 1
                j += 1
            if out1 - one <= cost:
                return True
        return False
    left = 0
    right = n
    res = 0x3f3f3f3f
    while left < right:
        mid = left + right >> 1
        if check(mid):
            right = mid
            res = min(res,mid)
        else:
            left = mid + 1
    print(res)
    t -= 1