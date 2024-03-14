#creation of array
array1 = [1,2,3, "Thimphu", 2.5]
print(array1)

#retrieving
element1 = array1[0]
element2 = array1[3]
lastElement = array1[-2]
print(lastElement)

#modifying elements
array1[0] = 10
print(array1)

#getting numbers of elements in an array
no_of_elements = len(array1)
print(no_of_elements)

#slicing 
elements = array1[0:3]
print(elements)

#concatenate lists
arr1 = [1,10]
arr2 = ["tphu", "wang"]
print(arr1 + arr2)

number_to_check = 1
result = number_to_check in arr1
print(result)

#add elements(append-adding from behind)
arrVariable = [1,2,3]
arrVariable.append(4)
print(arrVariable)

#insert at specific index(putting no in exact index)
arrVariable.insert(1,10)
print(arrVariable)

#sort(arrange from small to large)
arrVariable.sort()
print(arrVariable)

#pop(remove element)
arrVariable.pop(0)
print(arrVariable)

stackVar = []
#Adding stack
stackVar.append(4)
stackVar.append(6)
stackVar.append(3)
stackVar.append(1)
print('After appending', stackVar)
stackVar.pop(0)
print('After popping', stackVar)