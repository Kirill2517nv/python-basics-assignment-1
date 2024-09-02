# main.py

def calculate_sum(a, b):
    """
    Эта функция принимает два числа и возвращает их сумму.

    :param a: Первое число
    :param b: Второе число
    :return: Сумма a и b
    """
    return a + b


def main():
    # Пример использования функции calculate_sum
    number1 = 5
    number2 = 7
    result = calculate_sum(number1, number2)

    print(f"Сумма {number1} и {number2} равна {result}")


if __name__ == "__main__":
    main()