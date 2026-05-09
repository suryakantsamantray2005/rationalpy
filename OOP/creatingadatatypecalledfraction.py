#we are going to create a datatype of fraction 
#like 3/4*1/2=0.375 not 3/8
from math import gcd
class Fraction:
     def __init__(self,x,y):
          if y==0:
               raise ValueError("Denominator cannot be zero")
          if y<0:
               x=-x
               y=-y
          
          comm= gcd(x,y)

          self.num=x//comm
          self.den=y//comm

     def __str__(self):
          return '{}/{}'.format(self.num,self.den)
     
     def __add__(self,other):
          new_num=self.num*other.den + other.num*self.den
          new_den=self.den*other.den
          return Fraction(new_num,new_den)
     
     def __sub__(self,other):
          new_num=self.num*other.den - other.num*self.den
          new_den=self.den*other.den
          return Fraction(new_num,new_den)
     
     def __mul__(self,other):
          new_num=self.num*other.num
          new_den=self.den*other.den
          return Fraction(new_num,new_den)
     
     def __truediv__(self,other):

          if other.num==0:
               raise ZeroDivisionError("Cannot divide by zero")
          
          new_num=self.num*other.den
          new_den=self.den*other.num
          return Fraction(new_num,new_den)
     
     def convert_to_decimal(self):
          return self.num/self.den
     
     
     
fr1=Fraction(0,5)
fr2=Fraction(1,-8)
result=fr1*fr2
print(result)