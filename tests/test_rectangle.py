import pytest


def test_area(my_rectangle_one):
    assert my_rectangle_one.area() == 10 * 20

def test_perimeter(my_rectangle_one):
    assert my_rectangle_one.perimeter() == (10 + 20)*2

def test_not_standart(my_rectangle_one,my_rectangle_two):
    assert my_rectangle_one != my_rectangle_two