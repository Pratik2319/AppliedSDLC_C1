"""This is the main file for implementation"""
from dat_plo import *
from pr_email import *

def main():
    print("Calculating Data")
    auto_co_plotting([], [], "", "a")
    cross_co_plotting([], [], [],  "", "a")
    send_email()




if __name__ == "__main__":
    main()
    print("Email sent to all the students")
    print("Email sent to the Faculty")
