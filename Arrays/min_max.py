arr=list(map(int,input("Enter numbers:").split()))
sum=0
max=arr[0]
min=arr[0]
for i in arr:
    sum+=i
print(sum)
for i in range(len(arr)):
    if max<arr[i]:
        max=arr[i]
print(max)
for i in range(len(arr)):
    if min>arr[i]:
        min=arr[i]
print(min)