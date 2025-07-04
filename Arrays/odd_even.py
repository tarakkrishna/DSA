arr=list(map(int,input("Enter numbers:").split()))
even,odd=0,0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("even:",even)
print('odd:',odd)

