#Pattern in python
rows=int(input('ENTER THE NUMBER OF ROWS'))
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
print("")