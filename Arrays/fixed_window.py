arr = [4, 2, 1, 7]
max=0
for i in range(0,len(arr)-1):
    sum=arr[i]+arr[i+1]
    if sum>max:
        max=sum
print(max)