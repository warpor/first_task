import math
from abc import ABC, abstractmethod
from builtins import int
from typing import List, Union


class Figure(ABC):

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    def _check_values(self, value: Union[float, int]):
        if type(value) not in (float, int):
            raise TypeError("Values must be integers or float")
        if value <= 0:
            raise ValueError("Value must be positive")
        return value


class Circle(Figure):

    def __init__(self, radius: float):
        self.radius: float = self._check_values(radius)

    def calculate_area(self) -> float:
        return math.pi * (self.radius ** 2)


class Triangle(Figure):

    def __init__(self, side_a: float,
                 side_b: float, side_c: float):
        self.side_a: float = self._check_values(side_a)
        self.side_b: float = self._check_values(side_b)
        self.side_c: float = self._check_values(side_c)

    def calculate_area(self) -> float:
        half_perimeter: float = self.__calculate_half_perimeter()
        first_component: float = half_perimeter - self.side_a
        second_component: float = half_perimeter - self.side_b
        third_component: float = half_perimeter - self.side_c
        return (half_perimeter * first_component * second_component
                * third_component) ** 0.5

    def check_for_rectangular(self) -> bool:
        sorted_sides: List[float] = sorted([self.side_a, self.side_b, self.side_c])
        return sorted_sides[2] ** 2 == sorted_sides[0] ** 2 + sorted_sides[1] ** 2

    def __calculate_half_perimeter(self) -> float:
        return (self.side_a + self.side_b + self.side_c) / 2
