def i():
    n = int(input())
    st = []
    et = []
    for i in range(n):
        c = [int(z) for z in input().split(" ")]
        st.append(c[0])
        et.append(c[1])
    
    et, st = zip(*sorted(zip(et, st)))
    cet = et[0]
    output = 1

    for i in range(len(et)):
        if st[i]>=cet:
            cet = et[i]
            output+=1
    print(output)

i()