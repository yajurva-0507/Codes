x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print("*********MENU*********")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.exit")
print(" ")
while True:
    num=int(input())
    if num==1:
        print("Addition= ",x+y)
    elif num==2:
        print("Subtraction= ",x-y)
    elif num==3:
        print("Multiplication= ",x*y)
    elif num==4:
        print("Division= ",x/y)
    elif num==5:
        print("Code execution is completed")
        break
    else:   
        print("Invalid input")