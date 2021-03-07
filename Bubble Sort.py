a=[5,4,6,2,1]
length=len(a)

for i in range(length-1):
    for j in  range(length-i-1):
        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]

for i in range(length):
    print(a[i],end=" ")