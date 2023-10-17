arr = list(map(int,input().split()))
n = len(arr)
suf =[0 for _ in range(n)]
st = [n]
tot = 0
for i in range(n - 1,-1,-1):
    while len(st) > 1 and arr[st[-1]] - arr[i] < st[-1] - i:
        cur = st.pop()
        tot -= (2 * arr[cur] + st[-1] - cur - 1) * (st[-1] - cur)//2

    tot += (2 * arr[i] + st[-1] - i - 1) * (st[-1] - i)//2
    st.append(i)
    suf[i] = tot

s = sum(arr)
st = [-1]
tot = 0
for i in range(n):
    while len(st) > 1 and arr[st[-1]] - arr[i] < i - st[-1]:
        cur = st.pop()
        num = cur - st[-1]
        tot -=  (arr[cur] + arr[cur] + num - 1) * num // 2
    tot += (2 * arr[i] + i - st[-1] - 1) * (i - st[-1])//2
    st.append(i)
s = "dcd"
print(s[:len(s)-1])