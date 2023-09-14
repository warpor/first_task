# Figures calculation

Python библиотека предназначенная для подсчёта площади круга или треугольника.


## Использование

### класс Circle 

```python
from figures_calculation import Circle 

figure = Circle(3)  # Создаём круг с радиусом 3
print(figure.calculate_area())  # Вычисляем площадь и выводим ее на печать
```

### класс Triangle 

```python
from figures_calculation import Triangle 

figure = Triangle(3, 4, 5)  # Создаём треугольник со сторонами 3, 4, 5
print(figure.calculate_area())  # Вычисляем площадь и выводим ее на печать

print(figure.check_for_rectangular())  # Проверяем, является ли прямоугольник. 
```

## Расширение библиотеки

Для расширения библиотеки необходимо отнаследоваться от класса Figure и реализовать метод 
calculate_area().

### Пример

```python
from figures_calculation import Figure

class StrangeFigure(Figure):

    def calculate_area(self) -> float:
        area = 5    
        return area
```
