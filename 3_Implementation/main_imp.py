"""This is the main file for implementation"""
from dat_plo import *
from pr_email import *

#To get the dictionary of ps-no as key and mail as value 

ps_em = {}

def main():
    print("Calculating Data")
    

if __name__ == "__main__":
    main()
    calc_plot_all(ps_em)
    send_email(ps_em)
    print("Email sent to all the students")
    print("Email sent to the Faculty")
