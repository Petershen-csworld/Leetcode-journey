def pattern(needle):
    n = len(needle)
    m = [0 for _ in range(n)]
    c = 0
    for i in range(1,n):
        while c > 0 and needle[i] != needle[c]:
            c = m[c - 1]
        if needle[i] == needle[c]:
            c += 1
        m[i] = c
    return m
def kmp_search(t,pat):
    n = len(t)
    c = 0
    m = pattern(pat)
    for i,v in enumerate(t):
        while c > 0 and pat[c] != v:
            c = m[c - 1]
        if pat[c] == v:
            c += 1
