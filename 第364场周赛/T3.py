def comb(arr,tar):

    cur = [[] for _ in range(tar + 1)]
    cur[0].append([])

    for i in range(len(arr)):
        for c in range(tar,arr[i] - 1,-1):
            for item in cur[c - arr[i]]:
                add = item.copy()
                add.append(arr[i])
                cur[c].append(add)
    print(cur[7])

comb([1,2,4,5,6,7],7)