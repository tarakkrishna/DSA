import math
arr=list(map(int,input("Enter elements:").split()))
result=[]
for i in range(len(arr)):
    temp = []
    for j in range(len(arr)):
        if i!=j:
            temp.append(arr[j])
    result.append(math.prod(temp))
print(result)


