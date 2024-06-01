#Finding element in tuple
new_tuple=("a","b","c","d")
print("a" in new_tuple)
print("A" in new_tuple)
print(new_tuple.index("c"))
def search_tuple(tuple,element):
    for i in range(len(tuple)):
          if tuple[i] == element:
           return f"The {element} is found at the index{i}"
    return f"element {element} is not found"
search_tuple(new_tuple,"b")



