"""This is the main file for implementation"""
from dat_plo import *
from pr_email import send_email


# To get the dictionary of ps-no as key and mail as value
ps_em = {99003718:"prashantbagal191998@gmail.com"}


def main():
    "This is the main function"
    print("Calculating Data....")
    calc_plot_all_std(ps_em)
    #calc_plot_all_fac()
    send_email(ps_em)
    print("Sending Email.....")
    print("Email sent to all the students")
    print("Email sent to the Faculty")


if __name__ == "__main__":
    main()
