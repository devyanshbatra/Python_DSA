#EXCEPTION HANDLING
try:
    x=int(input("Enter the value of the first number"))
    y=int(input("Enter the value of the second number"))
    z=x/y
    print(z)
except ValueError:
    print("PLEASE ENTER THE CORRECT VALUE")
except ZeroDivisionError:
    print("you are dividing it with zero")
finally:
    var =z*100
    print(var)