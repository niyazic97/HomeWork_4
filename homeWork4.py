import math
import random


def test_greeting():
    name = "Анна"
    age = 25
    output = f"Привет, {name}! Тебе {age} лет."

    assert output == "Привет, Анна! Тебе 25 лет."
    print(output)


def test_rectangle():
    a = 10
    b = 20
    perimeter = (a + b) * 2
    assert perimeter == 60
    area = a * b
    assert area == 200


def test_circle():
    r = 23
    area = math.pi * r ** 2
    assert area == 1661.9025137490005
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list():
    """
    Создайте список из 10 случайных чисел от 1 до 100 и отсортируйте его по возрастанию.
    """
    l = [random.randint(1, 100) for i in range(10)]
    print("Исходный список:", l)
    l.sort()

    assert len(l) == 10
    assert l[0] < l[-1]

    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    # TODO удалите повторяющиеся элементы
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]
    l = list(set(l))
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_dicts():
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = dict(zip(first, second))

    assert isinstance(d, dict)
    assert len(d) == 5
    print(d)
