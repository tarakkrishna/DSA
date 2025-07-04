def frequency_with_visited():
    """
    Counts the frequency of each element in a list using nested loops and a visited list.
    Avoids printing duplicates by tracking already processed elements.
    """
    arr = list(map(int, input("Enter elements: ").split()))
    visited = []

    for i in arr:
        count = 0
        if i not in visited:
            for j in arr:
                if j == i:
                    count += 1
            print(i, '->', count)
            visited.append(i)


def frequency_with_dict():
    """
    Counts the frequency of each element in a list using a dictionary.
    More efficient than the nested loop method.
    Returns the dictionary with element-frequency pairs.
    """
    arr = list(map(int, input("Enter elements: ").split()))
    dic = {}

    for i in arr:
        if i not in dic:  # Check if element already exists in the dictionary
            dic[i] = 1     # First occurrence
        else:
            dic[i] += 1    # Increment count

    print(dic)
    return dic


# Uncomment the one you want to use:
#frequency_with_visited()
# frequency_with_dict()

#simpler code like above
arr=list(map(int,input('Enter elements:').split()))
target=int(input('Enter target:'))
count=0
for i in arr:
    if i==target:
        count+=1
if count==0:
    print('target not found')
else:
    print('target found',count,'times')