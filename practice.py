arr=list(map(int,input('Enter elements:').split()))
start=0
end=len(arr)-1
pal=True
while start<end:
    if arr[start]==arr[end]:
        start+=1
        end-=1
    else:
        pal=False
        break
if pal:
    print('palindrome')
else:
    print('not palindrome')

