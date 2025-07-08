arr=list(map(int,input('Enter elements:').split()))
visited=[]
dups=[]
for i in arr:
    if i not in visited:
        visited.append(i)
    else:
        dups.append(i)
print(dups)