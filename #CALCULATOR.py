
print("""Select the option : 
    1 : Add
    2: Subtract
    3: Multiply
    4: Divide
    """)

c = int(input())    


a = int(input("Enter 1st value : "))
b = int(input("Enter 2nd value : "))

if c == 1:
    print(a, " + ", b, " is : ", a + b)
elif c == 2:
    print(a, " - ", b, " is : ",a - b)
elif c == 3:
    print(a, " x ", b, " is : ",a * b)
elif c == 4:
    print(a, " / ", b, " is : ",a / b) 

