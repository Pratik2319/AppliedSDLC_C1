import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import openpyxl

Curpath = os.getcwd()

data1 = pd.read_excel(f"{Curpath}/3_Implementation/data_test/presurvey.xlsx")
data2 = pd.read_excel(f"{Curpath}/3_Implementation/data_test/postsurvey.xlsx")
data3 = pd.read_excel(f"{Curpath}/3_Implementation/data_test/pretest.xlsx")
data4 = pd.read_excel(f"{Curpath}/3_Implementation/data_test/posttest.xlsx")

data_all = [data1, data2, data3, data4]


def list_of_los(data,ps):
    """Perticular ps number los in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
        if data.iloc[i,0]==int(ps):
            for j in range(2,8):
               mylist.append(data.iloc[i,j])
            return mylist
        else:
            continue 


def average_of_los(data):
    '''average of all lo1,lo2,lo3,lo4,lo5,lo6 of all students in a list''' 
    mylist=[]
    for i in range(1,7):
        mystring="LO"+str(i)
        sum=data[mystring].mean()
        mylist.append(sum)
    return mylist


def min_of_LO(data):
    """minimum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list"""
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        min_lo=data[a].min()
        mylist.append(min_lo)
    return mylist


def max_of_LO(data):
    """maximum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list """
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        max_lo=data[a].max()
        mylist.append(max_lo)
    return mylist


def bottom_5_average(data):
    """average of bottom 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sorted_data=data.sort_values(string,axis=0)
        mea=sorted_data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


def top_5_average(data):
    """average of top 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sorted_data=data.sort_values(string,ascending=False)
        mea=sorted_data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


def sum_of_marks(data):
    """ Total marks in all los of students in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
            s=data.iloc[i,2:].sum()
            mylist.append(s)
    return mylist


def psno_email_list(data=data1):
    """Ps number corresponding email in a dictionary"""
    dic={}
    for i in range(0,data.shape[0]):
        dic[data.iloc[i,0]]=data.iloc[i,1]
    
    return dic


"""Plotting the data using bar graph"""
x_lst_all = ["LO1", "LO2", "LO3", "LO4", "LO5", "LO6"]


def auto_co_plotting(y_lst, y, a, x_lst=x_lst_all):
    """saves the plot in a given directory"""
    plt.bar(x_lst, y_lst, color="#ff0000")
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    #plt.legend()
    plt.title(a)
    try:
        path = f"{os.getcwd()}/3_Implementation/{y}"
        if not os.path.exists(path):
            os.mkdir(path)
        path_new = path + f"/{a}"
        plt.savefig(path_new)
    except Exception as e:
        print(e)
    

def cross_co_plotting(y_lst2, y_lst1, y, a, x_lst=x_lst_all):
    """to co-relate the data"""
    x_ind = np.arange(len(x_lst))
    width = 0.3
    plt.bar(x_ind, y_lst2, color="#ff0000", width=width)
    plt.bar(x_ind + width, y_lst1, color="#00ff00", width=width)
    plt.xlabel('Learning Objectives')
    plt.ylabel('Test/Survey points')
    #plt.legend()
    plt.title(a)
    try:
        path = f"{os.getcwd()}/3_Implementation/{y}"
        if not os.path.exists(path):
            os.mkdir(path)
        path_new = path + f"/{a}"
        plt.savefig(path_new)
    except Exception as e:
        print(e)


def calc_plot_all_std(d1):
    """plots all the plot for all students one at a time"""
    rd_lst = ["PRE_SURVEY", "POST_SURVEY", "PRE_TEST", "POST_TEST"]
    for student in d1.items():
        student_no = 0
        for data in data_all:                                                                          # PRE-TEST AND POST ASSESSMENT
            auto_co_plotting(list_of_los(data, student[0]), student[0], rd_lst[student_no])
            student_no += 1

        cross_co_plotting(list_of_los(data1, student[0]), list_of_los(data2, student[0]), student[0], "pre_pst_sur")  # CROSS B/W PRE AND POST SURVEY
        cross_co_plotting(list_of_los(data3, student[0]), list_of_los(data4, student[0]), student[0], "pre_pst_tst")  # CROSS B/W PRE AND POST ASSESSMENT


def calc_plot_all_fac():
    """plots all the plots required for the faculty"""
    s = "faculty"
    for data in data_all:
        cross_co_plotting(average_of_los(data), max_of_LO(data),s, "avg_max")
        cross_co_plotting(max_of_LO(data), min_of_LO(data),s, "max_min")
        cross_co_plotting(top_5_average(data), bottom_5_average(data),s, "tp_btm5")
