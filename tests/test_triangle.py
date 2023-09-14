import pytest

from figures import Triangle


def test_calculate_area_int():
    figure: Triangle = Triangle(3, 4, 5)
    area: float = figure.calculate_area()
    assert area == 6


def test_calculate_area_flaot():
    figure: Triangle = Triangle(3.5, 4, 5)
    area: float = figure.calculate_area()
    assert round(area,2) == 6.95


def test_for_rectangular():
    figure: Triangle = Triangle(3, 4, 5)
    assert figure.check_for_rectangular() == True


def test_for_incorrect_type():
    with pytest.raises(TypeError):
        figure: Triangle = Triangle(1, "str", 2)


def test_for_zero_value():
    with pytest.raises(ValueError):
        figure: Triangle = Triangle(0, 2, 1)


def test_for_negative_value():
    with pytest.raises(ValueError):
        figure: Triangle = Triangle(3, -4, 1)
