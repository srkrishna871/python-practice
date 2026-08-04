a=int(input("the value of a is : "))
b=int(input("the value of b is : "))
operators=(input("the operator is : "))

if operators == "+":
    print(a+b)
elif operators == "-":
    print(a-b)
elif operators == "*":
    print(a*b)
elif operators == "/":
    print(a/b)
else:
    print("invalid operator")
