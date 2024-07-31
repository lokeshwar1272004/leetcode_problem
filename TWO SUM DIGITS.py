a=[1,2,6,4]
target = 10
d={}
for i in range(len(a)):
    difference = target-a[i]
    if a[i] not in d:
        d[difference]=i
    else:
        print(d[a[i]],i)