#Traversing in a Dict
my_dict={'name': "raghav",'age':"16","Address":"faridabad"}
print(my_dict)
def traverse_dict(dict):
    for key in dict:
        print(key,dict[key])
traverse_dict(my_dict)