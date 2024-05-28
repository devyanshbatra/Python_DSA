#Searching in a list

my_dict={'name': "raghav",'age':"16","Address":"faridabad"}
print(my_dict)
def seach_dict(dict,value):
    for key in dict:
        if[key]==value:
         return key,value
        else:
           return ("key value doesnt exist")
print(seach_dict(my_dict,16))
