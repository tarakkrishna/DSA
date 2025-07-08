arr = list(map(int, input('Enter elements: ').split()))
k = int(input('Enter shift: '))
for i in range(k):
    # Take last element
    dig = arr[-1]
    # Insert at the front
    arr.insert(0, dig)
    # Remove last element (to avoid duplication)
    arr.pop()

print(arr)
