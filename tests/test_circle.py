import pytest

from figures_calculation import Circle


def test_calculate_area_int():
    figure: Circle = Circle(3)
    area: float = figure.calculate_area()
    assert round(area, 2) == 28.27


def test_calculate_area_flaot():
    figure: Circle = Circle(3)
    area: float = figure.calculate_area()
    assert round(area, 2) == 38.48



def test_for_incorrect_type():
    with pytest.raises(TypeError):
        figure: Circle = Circle("t")


def test_for_zero_value():
    with pytest.raises(ValueError):
        figure: Circle = Circle(0)


def test_for_negative_value():
    with pytest.raises(ValueError):
        figure: Circle = Circle(-4)
