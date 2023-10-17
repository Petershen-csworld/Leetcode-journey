t = int(input())
while t > 0:
    n = int(input())
    s = input()
    ##奇 奇 改变1个即可
    ##偶 偶 不动
    ##奇 偶 偶
    ##奇数借一个
    ##偶 奇 偶
    ##借一个
    ##偶 偶 奇
    ##直到下一个奇
    ##奇 偶 偶 奇
    ##奇 偶 奇 偶
    arr = []
    i = 0
    cur = s[0]
    while i < len(s):
        num = 0
        while i < len(s) and s[i] == cur:
            i += 1
            num += 1
        arr.append(num)
        if i < len(s):
            cur = s[i]
    m = 0
    i = 0

    while i < len(arr):
        if arr[i] % 2 == 1:

            while i < len(arr) and arr[i] % 2 == 1:
                i += 1
                m += 1

        else:
            i += 1
    print(m)




    t -= 1
