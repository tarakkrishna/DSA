arr = list(map(int, input('Enter elements: ').split()))
k = int(input('Enter shift: '))
for i in range(k):
    arr=arr[-k:]+arr[:-k]
print(arr)