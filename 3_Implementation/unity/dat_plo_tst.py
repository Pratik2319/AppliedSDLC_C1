import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import openpyxl


data1= pd.read_excel(r'''F:\Document\GitHub\AppliedSDLC_C1\3_Implementation\data_test\presurvey.xlsx''')



#Reading all the excel files presurvey,postsurvey,pretest and posttest

def list_of_los(data,ps):
    """Perticular ps number los in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
        if data.iloc[i,0]==ps:
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
        mylist.append(round(sum, 2))
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
        mylist.append(round(mea,2))
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

print(psno_email_list())