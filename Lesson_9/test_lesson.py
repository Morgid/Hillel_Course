# import pytest
# from lesson_9_my import add_two_nummbers
#
# def test_1():
#     assert add_two_nummbers(number_1=1, number_2=4) == 5
#
# def test_2():
#     assert add_two_nummbers(number_1=11, number_2=4) == 15
#
# def test_3():
#     assert add_two_nummbers(number_1=3, number_2=4) == 7

# # Solution 2
# @pytest.mark.parametrize("nomb_1, nomb_2, result", [
#     pytest.param(-4,4,0, id="Standart"),
#     pytest.param(11,-4,7, id="Negative"),
#     pytest.param(-3,-1,-4, id="Ololo")])
# def test_set_1(nomb_1,nomb_2,result):
#     assert add_two_nummbers(nomb_1, nomb_2) == result
#     pass
