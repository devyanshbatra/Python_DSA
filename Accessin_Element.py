import array
from array import *
arr1=array("i",[1,2,3,4,5])
def accessElement(array,index):
    if index > len(array):
     print("There is no elemnt in the array")
    else:
     print(array[index])
accessElement(arr1,4)
    