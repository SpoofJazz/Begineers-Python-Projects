# Simple calculator performing basic calculations
# For now performing basic operations going to modify soon
val1= eval(input("enter the number: "))
val2= eval(input("enter the number: "))
val3= input("enter any of the operators(+,-,*,/):")
result = 0
if val3=="+":
    result=val1+val2
elif val3=="-":
    result=val1+val2
    if val1>val2:
        result= val1 - val2
    else: 
        result= val2 - val1
elif val3=="*":
    result=val1*val2
elif val3=="/":
    result=val1/val2
else:
    print("invalid operator try using defined operators")
print("the result is: ",result)
