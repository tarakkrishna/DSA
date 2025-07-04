# Check if the input list is a palindrome using two-pointer technique

# Step 1: Take input and convert to list of integers
arr = list(map(int, input('Enter elements: ').split()))

# Step 2: Initialize pointers and flag
start = 0
end = len(arr) - 1
pal = True  # Assume it is a palindrome until proven otherwise

# Step 3: Compare elements from both ends
while start < end:
    if arr[start] == arr[end]:
        start += 1
        end -= 1
    else:
        pal = False  # Mismatch found
        break         # Exit loop immediately

# Step 4: Print result based on the flag
if pal:
    print('palindrome')
else:
    print('not palindrome')
