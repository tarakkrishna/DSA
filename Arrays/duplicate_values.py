# Find Duplicate Elements from a List Using Set

# Take input from user and convert to list of integers
arr = list(map(int, input('Enter elements: ').split()))

# Method 1 (Commented): Using nested loops to find duplicates
# dup = []
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[j] == arr[i]:
#             if arr[j] not in dup:
#                 dup.append(arr[j])
# print(dup)

# Method 2: Using set for better performance
x = set()        # Set to keep track of seen elements
dup = []         # List to collect duplicate elements

for i in arr:
    if i not in x:
        x.add(i)        # If element is not in set, add it
    else:
        dup.append(i)   # If already seen, it's a duplicate

# Print unique duplicates by converting the list to a set
print(list(set(dup)))
