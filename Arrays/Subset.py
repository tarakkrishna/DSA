arr1=list(map(int,input('Enter elements:').split()))
arr2=list(map(int,input('Enter elements:').split()))
subset=True
for i in arr2:
    if i in arr1:
        pass
    else:
        subset=False
        break
if subset==True:
    print(f'{arr2} is subset of {arr1}')
else:
    print(f'{arr2} is not a subset of {arr1}')