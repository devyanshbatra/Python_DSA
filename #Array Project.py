#Array Project
num_days= int(input("Enter the number of days "))
total=0
for i in range(1,num_days+1):
    next_day=input("days"+str(i)+3"s high temperature")
    total+=next_day
average=round(total/num_days)
print(num_days)
