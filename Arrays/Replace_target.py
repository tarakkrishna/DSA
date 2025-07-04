arr=list(map(int,input('Enter elements:').split()))
target=int(input('Enter target:'))
for i in range(len(arr)):
    if arr[i]==target:
        arr[i]=-1
print(arr)

