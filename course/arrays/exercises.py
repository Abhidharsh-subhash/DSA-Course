# 1. Create an array and Traverse
import array

print("step 1")
array1 = array.array("i", [1, 2, 3, 4, 5, 6, 7, 8])
for i in array1:
    print(i, end=" ")
# 2. Accessing individual elements through indexes
print("step 2")
print(array1[4])

# 3. Append any value to the array using append() method
print("step3")
array1.append(22)
print(array1)

# 4. insert value in an array using insert() method
print("step4")
array1.insert(3, 33)
print(array1)

# 5. Extend python array using extend() method
print("step5")
array2 = array.array("i", [51, 52, 53, 54, 55, 5])
array1.extend(array2)
print(array1)

# 6. Add items from list into array using fromlisit() method
print("step6")
list1 = [100, 101, 102, 103, 104, 105]
array1.fromlist(list1)
print(array1)

# 7. Remove any array element using remove() method
print("step7")
array1.remove(33)
print(array1)

# 8. Remove last array element using pop() method
print("step8")
array1.pop()
print(array1)

# 9. Fetch any element through its index using index() method
print("step9")
print(array1.index(55))

# 10. Reverse a python array using reverse() method
print("step10")
array1.reverse()
print(array1)

# 11. Get array buffer information through buffer_info() method
print("step 11")
print(array1.buffer_info())

# 12. Check the number of occurences of an element using count() method
print("step12")
print(array1.count(5))

# 13. convert array to string using tostring() method
print("step13")
tempstr = array1.tobytes()
print(tempstr)

# 14. convert array to a python list with same elements using tolist() method
print("step14")
templist = array1.tolist()
print(templist)

# 15. Slice elements from an array
print("step15")
print(array1[:4])
