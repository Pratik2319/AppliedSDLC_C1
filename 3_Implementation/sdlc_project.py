import pandas as pd
import matplotlib
data=pd.read_excel("presur.xlsx",header=1) """importing the presurvey file"""
print(data)
def average_of_los():
    """average of all lo1,lo2,lo3,lo4,lo5,lo6 of all students in a list """
    mylist=[]
    for i in range(1,7):
        mystring="LO"+str(i)
        sum=data[mystring].mean()
        mylist.append(sum)
    return mylist

#average_of_los()

def min_of_LO():
    """minimum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list"""
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        min_lo=data[a].min()
        mylist.append(min_lo)
    return mylist

# min_of_LO()

def max_of_LO():
    """maximum of all lo1,lo2,lo3,lo4,lo5,lo6 in a list """
    mylist=[]
    for i in range(1,7):
        a="LO"+str(i)
        max_lo=data[a].max()
        mylist.append(max_lo)
    return mylist

# max_of_LO()

def total_marks_of_student():
    """Total marks of all students in a list"""
    mylist=[]
    for i in range(0,data.shape[0]):
        av=data.iloc[i,2:].sum()
        mylist.append(av) 
    return mylist

# total_marks_of_student()


def bottom_5_average():
    """average of bottom 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sort_data=data.sort_values(string)
        mea=data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


# bottom_5_average()


def top_5_average():
    """average of top 5 students of a all los in a list """
    mylist=[]
    for i in range(1,7):
        string="LO"+str(i)
        sort_data=data.sort_values(string,ascending=False)
        mea=data.iloc[0:5,i+1].mean()
        mylist.append(mea)
    return mylist


#top_5_average()


def sum_of_marks():

    """ Total marks in all los of students in a list"""

     mylist=[]
     for i in range(0,data.shape[0]):
            s=data.iloc[i,2:].sum()
            mylist.append(s)
     return mylist


# sum_of_marks()