# Missing Number in Array
my_list=[1,2,3,4,55,6,7,8,9,11,12,13,14,15,16,17,18,19,20]
def missing_element(list,n):
    sum1=n*n+1/2
    sum2=sum(my_list)
    print(sum1-sum2)
missing_element(my_list,20)
