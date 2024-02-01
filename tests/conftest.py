import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle_one():
    return shapes.Rectangle(10,20)

@pytest.fixture
def my_rectangle_two():
    return shapes.Rectangle(1,2)