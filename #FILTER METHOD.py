#FILTER METHOD
def filter_1(a):
    if a%2==0:
        return True
    else:
        return  False
list(filter(filter_1,[10,20,30,68.99]))

def vowels(var):
    if var[-1] in "aeiou":
        return True
    else:
        return False
    
