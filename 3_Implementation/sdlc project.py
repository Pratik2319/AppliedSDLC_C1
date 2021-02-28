import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
data=pd.read_excel("presur.xlsx",header=1)
print(data)
#sum=data['LO1'].sum()
#no_of_rows=data.shape[0]
#average=sum/no_of_rows
#print(average)
def min_of_LO():
    """ returns minimum of a given LO across all the students"""
    for i in range(1,7):
        a="LO"+str(i)
        min_lo=data[a].min()
        return min_lo

min_of_LO()

def max_of_LO():
    """returns maximum of a given LO across all the students"""
    for i in range(1,7):
        a="LO"+str(i)
        max_lo=data[a].max()
        return max_lo

max_of_LO()

def total_marks_of_student():
    """returns total marks of a student across all LO'S"""
    for i in range(0,4):
        av=data.iloc[i,2:].sum()
        return av   

total_marks_of_student()


"""Do not touch this yet"""
"""Plotting the data using bar graph"""

x_lst_all = ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6"]

def auto_co_plotting(y_lst, x_lst, y):
    plt.bar(x_lst, y_lst, color="#000000", label="Student's Performance")
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    path = f"C:/Users/mithu/Desktop/demo/{y}"
    os.mkdir(path)
    plt.savefig(f"{y}/plot.png")


def cross_co_plotting(y_lst2, y_lst1, x_lst):
    x_ind = np.arange(len(x_lst))
    width = 0.3
    plt.bar(x_ind, y_lst2, color="#000000", label="Pre-test", width=0.3)
    plt.bar(x_ind + width, y_lst1, color="#ff00ff", label="Post-test", width=0.3)
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    plt.savefig()





