an="arn:aws:iam::15848069:name/johnny"
b=(an.split("/")[1]) #--> splits the arn variable at / and takes the index 1 value
c=b[0] #--> prints the index 0 of variable b
print(b.upper()) #--> variable.upper() is doing upper case of variable passed.
print(c)

#a="hello"
#b="world"
#c=a+" "+b
#print(c.split(" ")[1].upper())

#length of arn and c combined
#d=len(an)+len(c) #d is storing the length of arn and c combined

#print("the length of an is :",len(an))
#print("The length of c is :",len(c))
#print("The total length of arn and c is :",d)

