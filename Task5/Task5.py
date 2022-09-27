# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

from math import sqrt
print('Введите координаты точки a:')
x_a = float(input('X: '))
y_a = float(input('Y: '))
print("Введите координаты точки b:")
x_b = float(input('X: '))
y_b = float(input('Y: '))

print('Расстояние между a и b: ', round(
    sqrt((x_a - x_b)**2 + (y_a - y_b)**2), 2))
