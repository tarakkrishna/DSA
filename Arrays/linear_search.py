arr=list(map(int,input('Enter elements:').split()))
target=int(input('Enter target:'))
found=False
for i in arr:
    if target==i:
        print('element at indexs:',arr.index(i))
        found=True
if found!=True:
    print('target not found')

#using enumerate
# arr=list(map(int,input('Enter elements:').split()))
# target=int(input('Enter target:'))
# found=False
# for i,v in enumerate(arr):
#     if target==v:
#         print('element at index:',i)
#         found=True
#         break
# if found!=True:
#     print('target not found')


# every index of number
# arr=list(map(int,input('Enter elements:').split()))
# target=int(input('Enter target:'))
# found=False
# for i,v in enumerate(arr):
#     if target==v:
#         print('element at indexs:',i)
#         found=True
# if found!=True:
#     print('target not found')