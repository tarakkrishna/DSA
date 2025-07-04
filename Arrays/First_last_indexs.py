arr=list(map(int,input('Enter elements:').split()))
target=int(input('Enter target:'))
found=False
first,last=0,0
for i,v in enumerate(arr):
    if v==target:
        last=i
        found=True
if found:
    first=arr.index(target)
    print(first,last)

