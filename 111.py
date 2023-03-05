from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')


def сalculate_square_root(num: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(num)


def calc(your_number: float):
    """Расчет."""
    if your_number <= 0:
        root: float = сalculate_square_root(0)
        return root
    root: float = сalculate_square_root(your_number)
    return (f'Мы вычислили квадратный корень из введённого вами числа. '
            f'Это будет: {root}')


print(message)
print(calc(25.5))
