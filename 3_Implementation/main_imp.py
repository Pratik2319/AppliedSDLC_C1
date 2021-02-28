"""This is the main file for implementation"""
from dat_plo import *
from pr_email import *
import csv

#To get the dictionary of ps-no as key and mail as value 

def main():
    print("Calculating Data")
    auto_co_plotting([], [], "", "a")
    cross_co_plotting([], [], [],  "", "a")
    send_email()




if __name__ == "__main__":
    main()
    print("Email sent to all the students")
    print("Email sent to the Faculty")
