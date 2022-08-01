import array as arr
a = arr.array('i', [1,2,3])
print("The new created array is : ", end= " ")
for i in range(0,3):
    print (a[i], end= " ")
print()
b = arr.array('d', [2, 4,6,8,10])
print("The new created array is: ", end= " ")
for i in range (0,4):
    print (b[i], end= " ")
b.append(4.4)
print ("Array after insertion : ", end = " ")
for i in b:
    print(i, end = " ")
print()
c = arr.array('i',[2,3,4,5,6,7,])
print("Access element is: ", c[0])
print("Access element is: ", c[3])

print("The new created array is: ", end= " ")
for i in range (0, 5):
    print(arr[i], end =" ")
print("\r")
print("the popped element is: ", end =" ")
print(arr.pop(2))
print("The array after popping is: ", end = " ")
for i in range (0, 4):
    print(arr[i], end = " ")
print("\r")


