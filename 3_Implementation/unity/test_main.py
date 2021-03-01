"""This is for Unit/ Python testing """


from dat_plo_tst import *
import pytest

#read from presurvey
data = pd.read_excel("presurvey.xlsx")

def test_fun():
    assert list_of_los(data,99003650) == [9,7,5,6,7,0]
    pass

def test_fun1():
    assert average_of_los(data) == [7.87,6.67,7.27,7.87,6.8,8]
    pass

def test_fun2():
    assert min_of_LO(data) == [5,0,1,2,0,0]
    pass 

def test_fun3():
    assert max_of_LO(data) == [10,10,10,9,10,10]
    pass

def test_fun5():
    assert bottom_5_average(data) == [5.8, 3.0, 3.8, 6.4, 3.4, 5.6]
    pass

def test_fun6():
    assert top_5_average(data) == [9.2,9.4,9.6,9,9,9.6]
    pass

def test_fun7():
    assert sum_of_marks(data) == [35,34,47,47,43,45,49,42,49,45,43,53,53,46,36]
    pass
