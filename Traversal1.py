import array
arr1=array.array("i",[1,2,3,4,5,6])
arr2=array.array("d",[7,8, 9,10,11,12])
def traverseArray(array):
    for i in array:
        print(i)
traverseArray(arr1)