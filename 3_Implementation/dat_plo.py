import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import openpyxl

#Reading all the files
data1=pd.read_excel("data_test/presurvey.xlsx")
data2=pd.read_excel("data_test/postsurvey.xlsx") 
data3=pd.read_excel("data_test/pretest.xlsx")
data4=pd.read_excel("data_test/posttest.xlsx")

data = [data1, data2, data3, data4]

def marks_los(data, psno):
    pass

def average_of_los(data):
    '''average of all lo1,lo2,lo3,lo4,lo5,lo6 of all students in a list''' 
    mylist=[]
    for i in range(1,7):
        mystring="LO"+str(i)
        sum=data[mystring].mean()
        mylist.append(sum)
    return mylist

#average_of_los()

def min_of_LO(data):
    """minimum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list"""
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        min_lo=data[a].min()
        mylist.append(min_lo)
    return mylist

# min_of_LO()

def max_of_LO(data):
    """maximum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list """
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        max_lo=data[a].max()
        mylist.append(max_lo)
    return mylist
# total_marks_of_student()


def bottom_5_average(data):
    """average of bottom 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sorted_data=data.sort_values(string,axis=0)
        mea=sorted_data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


# bottom_5_average()


def top_5_average(data):
    """average of top 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sorted_data=data.sort_values(string,ascending=False)
        mea=sorted_data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


# top_5_average()


def sum_of_marks(data):

    """ Total marks in all los of students in a list"""

    mylist=[]
    for i in range(0,data.shape[0]):
            s=data.iloc[i,2:].sum()
            mylist.append(s)
    return mylist


# sum_of_marks()
def psno_email_list(data=data1):
    """Ps number corresponding email in a dictionary"""
    dic={}
    for i in range(0,data.shape[0]):
        dic[data.iloc[i,0]]=data.iloc[i,1]
    
    return dic

print(dic)

"""Plotting the data using bar graph"""
x_lst_all = ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6"]


def auto_co_plotting(y_lst, y, a, x_lst=x_lst_all):
    """saves the plot in a given directory"""
    plt.bar(x_lst, y_lst, color="#000000", label="Student's Performance")
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    if not os.path.exists(f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"):
        path = f"C:/Users/mithu/AppliedSDLC_C1/3_Implementation/{y}"
        os.mkdir(path)
    plt.savefig(f"{y}/{a}.png")


def cross_co_plotting(y_lst2, y_lst1, y, a, x_lst=x_lst_all):
    """to co-relate the data"""
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


def calc_plot_all_std(d1):
    """plots all the plot for a all students one at a time"""
    rd_lst = ["pre_sur", "post_sur", "pre_tst", "post_tst"]
    for d in d1.items():
        j = 0
        for i in data:                                                                           #PRE-TEST AND POST ASSESSMENT
            auto_co_plotting(marks_los(i, d[0]), d[0], rd_lst[j])
            j += 1

        cross_co_plotting(marks_los(data1, d[0]), marks_los(data2, d[0]), d[0], "pre_post_sur")  #CROSS B/W PRE AND POST SURVEY
        cross_co_plotting(marks_los(data3, d[0]), marks_los(data4, d[0]), d[0], "pre_post_tst")  #CROSS B/W PRE AND POST ASSESSMENT


def calc_plot_all_fac():
    """plots all the plots required for the faculty"""
    s = "faculty"
    for i in data:
        cross_co_plotting(average_of_los(i), max_of_LO(i),s, "avg_max")                        #CROSS B/W AVERAGE AND CLASS MAXIMA
        cross_co_plotting(average_of_los(i), min_of_LO(i),s, "avg_min")                        #CROSS B/W AVERAGE AND CLASS MINIMA
        cross_co_plotting(top_5_average(i), bottom_5_average(i),s, "tpmax_min")                #CROSS B/W TOP_5 AND BOTTOM_5

