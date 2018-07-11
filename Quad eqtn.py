#Project for codeLagos - Oluwasegun ROTIMI

print( "This is a program that solves mathematical problems using the Almighty Formular \n")
print(('*'*7)+"Welcome , Kindly follow the prompt below"+('*'*7))
       
import math
a=int(input("Enter a value for a : "))
b=int(input("Enter a value for b : "))
c=float(input("Enter a value for c : "))

d= b**2-4*a*c #discriminating factor
if (d<0): #it cannot be solved using the quadratic equation
                print("This equation has no solution")
elif (d==0):
                x=(-b+math.sqrt(b**2-4*a*c))/2*a
                print("there is only one solution," , x )
else:
                x1= (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
                x2= (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
                print("There are 2 solutions ; " , x1, "or" ,x2)
                      
              


