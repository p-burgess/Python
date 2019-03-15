#Abdulaziz .M. Abdallah
#Student No:12052839
#Assignment:1
creditcard=str(input("Please enter a credit card number "))
while (len(creditcard)!= 8)or(len(creditcard)<0):
    creditcard=str(input("Please enter a credit card number again "))

A=int(creditcard[7:8:])
B=int(creditcard[5:6:])
C=int(creditcard[3:4:])
D=int(creditcard[1:2:])
#print(A,B,C,D)
sum=A+B+C+D
    
E=int(creditcard[6:7:])*2
if (E > 9):
    ee = E-10+1
else:
    ee = E
        
F=int(creditcard[4:5:])*2
if (F > 9):
    ff = F-10+1
else:
    ff = F

G=int(creditcard[2:3:])*2
if (G > 9):
    gg = G-10+1
else:
    gg = G

H=int(creditcard[0:1:])*2
if (H > 9):
    hh = H-10+1
else:
    hh = H
#print(ee,ff,gg,hh)
    
Total=A+B+C+D+ee+ff+gg+hh

#print(Total)

if int(Total) > 10 :
    if (int(str(Total)[1:2]))<int(creditcard[7:8]):
        checkdigit=int(creditcard [7:8]) - int(str(Total)[1:2])
    elif(int(str(Total)[1:2])==int(creditcard[7:8])):
        checkdigit=0
    else:
        checkdigit=int((10-int(Total[1:2]))) + int(creditcard[7:8])
elif int(Total) == 10:
    checkdigit = 0
else:
    checkdigit= (10- int(str(Total)))+int(creditcard[7:8])
    if checkdigit == 10 :
        checkdigit = 0
    else:
        checkdigit = checkdigit
            
if (Total % 10 ==0):
    print("The number is valid")
else:
    
     print("The number is invalid ")
     print("correct number:",creditcard[:7:]+str(checkdigit))
    
