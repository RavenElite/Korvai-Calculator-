import math
import numpy as np
z = 1
#SOLUTIONS = []
m = input("Enter Thalam or its Aksharam Count: ")
n = input("Enter Edipu in Terms of Aksharams: ")
a = input("Enter 1st Round's Nadai: ")
b = input("Enter 2nd Round's Nadai: ")
c = input("Enter 3rd Round's Nadai: ")

m = m.lower()
if m == "rupakam":
    m = 3
if m == "rupaka thalam":
    m = 3
if m == "adi":
    m = 8
if m == "adi thalam":
    m = 8
if m == "kandam":
    m = 5
if m == "kanda chap":
    m = 5
if m == "misram":
    m = 7
if m == "misra chap":
    m = 7
if m == "ata thalam":
    m = 14
if m == "adi thalam 2 kalai":
    m = 16
   
m = float(m)
n = float(n)
a = float(a)
b= float(b)
c= float(c)

y = (b * c + a * c  + b * a )  
y = y/ (a*b*c)

while z<100:
    if z == 1:
        print ("Here are all Possible Solutions:")
    x = ((m * z) + n)  / (y)
    x = str(x)
    d = x.split (".")
    if int(d[-1]) == 0:
        x = float(x)
        x = str(x)
        x = x[:-2]
        print (x)
        x = [x]
        #SOLUTIONS = np.append (SOLUTIONS, x)
    z = z + 1