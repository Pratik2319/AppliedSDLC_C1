import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt

data=pd.read_excel("presur.xlsx",header=1)
print(data)

def average_of_los():
    """average of all lo1,lo2,lo3,lo4,lo5,lo6 of all students in a list """
    mylist=[]
    for i in range(1,7):
        mystring="LO"+str(i)
        sum=data[mystring].mean()
        mylist.append(sum)
    return mylist


def min_of_LO():
    """minimum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list"""
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        min_lo=data[a].min()
        mylist.append(min_lo)
    return mylist


def max_of_LO():
    """maximum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list """
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        max_lo=data[a].max()
        mylist.append(max_lo)
    return mylist


def total_marks_of_student():
    """Total marks of all students in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
        av=data.iloc[i,2:].sum()
        mylist.append(av) 
    return mylist


def bottom_5_average():
    """average of bottom 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sort_data=data.sort_values(string)
        mea=data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


def top_5_average():
    """average of top 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sort_data=data.sort_values(string,ascending=False)
        mea=data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


def sum_of_marks():
    """ Total marks in all los of students in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
            s=data.iloc[i,2:].sum()
            mylist.append(s)
    return mylist

#-----------------------------------------------------------------------------------------------------------

"""Do not touch this yet"""
"""Plotting the data using bar graph"""

x_lst_all = ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6"]


def auto_co_plotting(y_lst, x_lst, y, a):
    """saves the plot in a given directory"""
    for i in y_lst:
        if type(i) != int:
            pass               #Todo for dummy/missing data
    plt.bar(x_lst, y_lst, color="#000000", label="Student's Performance")
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    if not os.path.exists(f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"):
        path = f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"
        os.mkdir(path)
    plt.savefig(f"{y}/{a}.png")

    """Will use later"""
    return f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"


def cross_co_plotting(y_lst2, y_lst1, x_lst, y, a):
    """to co-relate the data"""
    for i in y_lst1:
        if type(i) != int:
            pass               #Todo for dummy/ missing data
    x_ind = np.arange(len(x_lst))
    width = 0.3
    plt.bar(x_ind, y_lst2, color="#000000", label="Pre-test", width=0.3)
    plt.bar(x_ind + width, y_lst1, color="#ff00ff", label="Post-test", width=0.3)
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    if not os.path.exists(f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"):
        path = f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"
        os.mkdir(path)
    plt.savefig(f"{y}/{a}.png")
    
    """Will use later"""
    return f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"




