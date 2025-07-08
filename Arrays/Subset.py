arr1=list(map(int,input('Enter elements:').split()))
arr2=list(map(int,input('Enter elements:').split()))
subset=True
d1,d2={},{}
for i in arr1:
    if i not in d1:
        d1[i]=1
    else:
        d1[i]+=1

for j in arr2:
    if j not in d2:
        d2[j]=1
    else:
        d2[j]+=1

for i in d2:
    if i not in d1 or d2[i]>d1[i]:
        subset=False
        break
    else:
        pass

if subset:
    print(f'{d2} is subset of {d1}')
else:
    print(f'{d2} is not subset of {d1}')