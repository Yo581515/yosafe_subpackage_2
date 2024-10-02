
from yosafe_packages.yosafe_subpackage_2.yosafe_subpackage_2_functions import yosafe_sub, to_capitllal_letters_2, yosafe_get_yosafe_subpackage_2
from yosafe_packages.yosafe_subpackage_1.yosafe_subpackage_1_functions import yosafe_add



def test_yosafe_get_yosafe_subpackage_2():
    result = yosafe_get_yosafe_subpackage_2()
    print(result)
    assert "Error" not in result



def test_yosafe_add():
    assert yosafe_sub(99, 99) == 0
    assert yosafe_sub(-3, 1) == -4


def test_to_capitllal_letters_2():
    assert to_capitllal_letters_2("hello") == "HELLO"
    assert to_capitllal_letters_2("hello world") == "HELLO WORLD"
    assert to_capitllal_letters_2("hello world!") == "HELLO WORLD!"

def test_yosafe_add():
    assert yosafe_add(99, 99) == 198