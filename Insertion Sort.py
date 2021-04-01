a=[5,4,6,2,1]
length=len(a)
for i in range(1,length):
    key=a[i]
    j=i-1
    while(j>=0 and key<a[j]):
        a[j+1]=a[j]
        j-=1
    a[j+1]=key

for i in range(length):
    print(a[i],end=" ")
