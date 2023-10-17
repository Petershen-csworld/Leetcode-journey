a= [ 2,4,5,13,24,32]
s = []
def permu(i,chosen,st):
    if i == len(a):
       if chosen == 3:
            print(st)
       return
    st.append(a[i])
    permu(i + 1,chosen + 1,st)
    st.pop()
    permu(i + 1,chosen,st)
permu(0,0,s)