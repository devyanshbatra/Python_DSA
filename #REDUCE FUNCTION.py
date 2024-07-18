#REDUCE FUNCTION
list_num=[12,12,45,76,89,76,66,54]
def reduce_first(var1,var2):
    return var1+var2
from functools import reduce
reduce(reduce_first,list_num)
