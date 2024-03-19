# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 09:05:20 2024

@author: Dustin Miller
"""

#Algorithms – Programming Assignment #1
import random
import time
from tabulate import tabulate

#One-Dimensional Particle Function
## Function will simulate random steps in 1st dimension for any # of steps
def one_dim_simulation(step_num):
    x = 0
    for i in range(step_num):
        shift = random.choice([-1,1])
        x += shift 
        if x == 0:
            return True
    return False
    
    
#Two-Dimensional Particle Function
## Function will simulate random steps in 2nd dimension for any # of steps
def two_dim_simulation(step_num):
    x = 0
    y = 0
    for i in range(step_num):
        axis = random.choice([1,2])
        shift = random.choice([-1,1])
        if axis == 1:
            x+= shift 
        else: 
            y+= shift
        if x == 0 and y==0:
            return True
    return False
    
#Three-Dimensional Particle Function
## Function will simulate random steps in 3rd dimension for any # of steps
def three_dim_simulation(step_num):
    x = 0
    y = 0
    z = 0
    for i in range(step_num):
        axis = random.choice([1,2,3])
        shift = random.choice([-1,1])
        if axis == 1:
            x += shift 
        elif axis == 2:
            y += shift
        else:
            z += shift
        if x == 0 and y==0 and z==0:
            return True
    return False

#Numerical Testing Function 
## Test the % of time particle returns given x number of steps
def test_function(amount_of_steps, dimension_function):
    true_result = 0
    total_result = 0
    for i in range(100):
        result = dimension_function(amount_of_steps)
        total_result += 1
        if result == True:
            true_result += 1
    percentage = (true_result/total_result)*100
    return percentage


def main():
    step_num = [20, 200, 2000, 20000, 200000, 2000000]
    dim_list = [one_dim_simulation, two_dim_simulation]
    data_list  = []
    for dimension in dim_list:
        for number in step_num:
            result = test_function(number, dimension)
            data_list.append(result)
    time_list = []       
    for number in step_num:
        start_time = time.time()
        result = test_function(number, three_dim_simulation)
        data_list.append(result)
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_list.append(elapsed_time)
        
    list_dim_one = ['1D', data_list[0],data_list[1], data_list[2],data_list[3],data_list[4],data_list[5]]
    list_dim_two = ['2D', data_list[6],data_list[7], data_list[8],data_list[9],data_list[10],data_list[11]]
    list_dim_three = ['3D', data_list[12],data_list[13], data_list[14],data_list[15],data_list[16],data_list[17]]
    time_list_data = ['Run Time 3D (Seconds)', time_list[0],time_list[1], time_list[2],time_list[3],time_list[4],time_list[5]]
    data = [list_dim_one, list_dim_two, list_dim_three, time_list_data]
    headers = ["Number of Steps", "20", "200", "2000", "20000", "200000", "2000000", ]
    table = tabulate(data, headers, tablefmt="grid")
    print(table)


main()

    