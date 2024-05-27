# if condition list comprehension
prev_list=[1,2,-3,-4,5,6,-7]
new_list=[number for number in prev_list if number>0 ]
print(new_list)
new_list1=[number*number for number in prev_list if number<0]
print(new_list1)
