x=list(map(int,input('Enter elements:').split()))
largest=x[0]
for i in x:
    d=len(str(i))
    if len(str(largest))<d:
        largest=i
print(largest)

