from math import sqrt

message = ('Добро пожаловать в самую лучшую программу '
           'для вычисления квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Расчёт квадратного корня."""
    calc_number = calculate_square_root(your_number)
    if your_number <= 0:
        return
    print('Мы вычислили квадратный корень из введенного вами числа. '
          f'Это будет: {calc_number}')


print(message)
calc(25.5)
