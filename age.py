a=12
b=30
c=365
a1=int(input("Enter your age in years:"))
a2=int(input("Enter you age in months above the given years:"))
a3=int(input("Enter your age in days above the given months:"))
a4=a1*a+a2
a5=a1*c+a2*b
print("Your age in years is: ", a1)
print("Your age in months is: ", a4)
print("Your age in days is: ", a5) 
print(f"That is {a1} years or,{a4} months or,{a5} days")  