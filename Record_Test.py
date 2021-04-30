import pytest
from FUNCTION import *


def test_add_new_Data():
    assert add_new_Data() == "new_Data_added"


def test_show_Data():
    assert show_Data() == "displayed"


def test_find():
    RECORD = open("RECORD", "rb")
    Data_list = pickle.load(RECORD)
    find_name = "264002"
    is_Data_found = False
    assert find(Data_list,find_name,is_Data_found) != "not_found"
    RECORD.close()
