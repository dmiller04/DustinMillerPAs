# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:14:28 2024

@author: Dustin Miller
"""

### PART 1
#2
import numpy as np 

#4: 𝑓(𝑥) = 2𝑥^3 + 3𝑥^2 + 1
def print_polynomial(list_coeff):
    poly = np.poly1d(list_coeff)
    print('The polynomial is expressed as: ')
    print(f'{poly}')
    print()
    
def solve_polynomial(poly, x):
    return np.polyval(poly, x)

print_polynomial([2,3,0,1])
print(solve_polynomial([2,3,0,1],2))
print()

#5 𝑓(𝑥) = 𝑥^2 + 1
def print_derivative(list_coeff, x):
    poly = np.poly1d(list_coeff)
    derivative = np.polyder(poly)
    answer = solve_polynomial(derivative, x)
    print(f'The derivative evaluated at {x} is {answer}')
    print()
    
print_derivative([1,0,1], 1)

### PART 2
    
def solve_derivative(polynomial, x):
    derivative = np.polyder(polynomial)
    return np.polyval(derivative, x)
    
def calculate_next_x(old_x, polynomial):
    numerator = solve_polynomial(polynomial, old_x)
    denominator = solve_derivative(polynomial, old_x)
    return round(old_x - (numerator/denominator),3)

def newtons_method(polynomial, x, count=1, margin_of_error=.001):
    print(f'x{count} = {x} ')
    x_next = calculate_next_x(x, polynomial)
    if abs(x - x_next) < margin_of_error:
        print(f'x{count+1} = {x_next} ')
        return print(f'The final value with stablized thousandths place is {x_next}')
    else:
        return newtons_method(polynomial, x_next, count+1, .001)
        
def main():
    input_poly = input("Enter coefficients for polynomial seperated by comma: ")
    coeff = input_poly.split(',')
    for i in range(len(coeff)):
        coeff[i] = int(coeff[i])
    x1 = int(input("Enter x1: "))
    polynomial = np.poly1d(coeff)
    newtons_method(polynomial, x1)
    roots = np.roots(coeff)
    print()
    print(f'The roots calculated with the roots function are {roots}')
    
main()


    