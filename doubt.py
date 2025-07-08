d1={}
arr1=[1,2,4,5,2,5]
for i in arr1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1
print(d1)