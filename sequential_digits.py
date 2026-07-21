low = 100
high = 300
res = []
strr = "123456789"


l,r = 0,1
while l<len(strr):
    st = strr[l:r]
    if st == "":
        break
    if low<int(st)<high:
        res.append(int(st))
        r+=1
    elif int(st)<low:
        r+=1
    
    
    if r>len(strr):
        l +=1
        r = l+1

print(res)