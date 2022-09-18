## Add code below with answer clearly stated
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 17:11:27 2022

@author: Umer Yasin
"""

# Question 1
import math

def sum_fact_digits(n):
  
  try:
    
    #Call fact function
    fact = math.factorial(int(n))
    
    #Convert this number to string --> int
    Sum = sum(map(int, str(fact)))
    
    print("Sum of digits is:",Sum)
    
  except:
      print("Error: Please enter value greater or equal to zero !!")
  
      
if __name__ == '__main__':
  num = input("Enter number to find the sum of factorial digits:")
  
  # Find the sum of the digits in the number 100!
  sum_fact_digits(num)    
  
  # Video link:
  
  # https://drive.google.com/file/d/1GPP-DTu1Cmbu6--vOuMh8h6pbUfCeRRh/view?usp=sharing
