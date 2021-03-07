a=[5,4,6,2,1]
length= len(a)
print("List before sorting:",end="")
for i in range(length):
    print(a[i],end=" ")
for i in range(length):
    min_index=i
    for j in range(i+1,length):
        if(a[j]<a[min_index]):
            min_index=j

    a[i],a[min_index]=a[min_index],a[i]
    i+=1
print("\nList after sorting:",end="")
for i in range(length):
    print(a[i],end=" ")