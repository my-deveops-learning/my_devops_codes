#Loops cases:

##data = [0,1,2,3,4,5]

#for a in data:
    #print (f" inside for loop value of data plus one is : {a + 1}")
    #while (a <= 4):
        #print (f"inside while loop value of data is: {a}")
        #break

#count = 0

#while ( count < 5):
    #print (f" inside while loop count value is : {count}")
    #count += 1

#count = 0
#while count < 5:
    #for a in range(5):
        #print ("*", end=" ")
    #print ("\n")
    #count += 1

countv = 0
countc = 5
while countv < 5:
    for a in range(countc):
        print ("*", end=" ")
    countc -= 1
    print ("\n")
    countv += 1

countv = 0
countc = 1
while countv < 5:
    for a in range(countc):
        print ("*", end=" ")
    countc += 1
    print ("\n")
    countv += 1

