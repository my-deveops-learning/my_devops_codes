import sys

def compare(a,b):
    if (a>b):
        print (f"here a is {a} and b is {b} and",f"{a} is greater than {b}")
    elif (a<b):
        print (f"here a is {a} and b is {b} and",f"{b} is greater than {a}")
    elif (a == b):
        print (f"here a is {a} and b is {b} and",f"{a} is equal to {b}")
    
c = float(sys.argv[1])
d = float(sys.argv[2])  
compare(c,d)