# PRINTING FIBONACCI SERIES UPTO NUMBER 10
terms=10
a=0
b=1
count=0
tup=()
if terms<= 0:
    print("please enter a positive integer")
elif terms== 1:
    print("fibonacci series up to",terms)
    print(a)
else:
    print("fibonacci series up to",terms)
    while count < terms:
        tup=tup + (a, )
        nth=a + b
        a=b
        b=nth
        count += 1
        print(tup)
