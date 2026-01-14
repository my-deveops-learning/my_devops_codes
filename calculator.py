#a = 5
#b = 10
import sys

def add(a,b):
    add = a + b
    #print ("Addition is :", add)
    return add

def subtract(b,a):
    s = b - a
    #print ("Subtraction is :", s)
    return s

def multiply(b,a):
    m = a * b
    #print ("Multiplication is :", m)
    return m

def divide(b,a):
    d = b / a
    #print ("Division is :", d)
    return d

#u = add(5,10)
#print ("Addition is :", u)
#v = subtract(10,5)
#print ("Subtraction is :", v)
#x = multiply(10,5)
#print ("Multiplication is :", x)
#y = divide(10,5)
#print ("Division is :", y)
#print ("Addition is :", add(5,10), "\nSubtraction is :", subtract(10,5), "\nMultiplication is :", multiply(10,5), "\nDivision is :", divide(10,5))

num1 = float(sys.argv[1])
op = sys.argv[2]
num2 = float(sys.argv[3])

if op == ("+" or "add"):
    print("Addition is :", add(num1,num2))

elif op == ("-" or "sub"):
    print("Subtraction is :", subtract(num2,num1))

elif op == ("*" or "mul"):
    print("Multiplication is :", multiply(num1,num2))

elif op == ("/" or "div"):
    print("Division is :", divide(num2,num1))

else:
    print("Invalid operator")