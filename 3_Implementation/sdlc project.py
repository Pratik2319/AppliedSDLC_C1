import pandas as pd
import matplotlib
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