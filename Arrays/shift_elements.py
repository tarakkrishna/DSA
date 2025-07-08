# arr = list(map(int, input('Enter elements: ').split()))
# k = int(input('Enter shift: '))
# for i in range(k):
#     # Take last element
#     dig = arr[-1]
#     # Insert at the front
#     arr.insert(0, dig)
#     # Remove last element (to avoid duplication)
#     arr.pop()
#
# print(arr)
#




# # This program performs a right rotation of elements in a list by k positions
#
# # Input: space-separated integers (the list elements)
# arr = list(map(int, input('Enter elements: ').split()))
#
# # Input: number of times to rotate the list to the right
# k = int(input('Enter shift: '))
#
# # Perform rotation k times
# for i in range(k):
#     # Split the list into two parts using slicing:
#     # arr[-k:] gives the last k elements (to bring to front)
#     # arr[:-k] gives the rest of the list (to shift to back)
#     arr = arr[-k:] + arr[:-k]
#
# # Output: rotated list
# print(arr)
#
