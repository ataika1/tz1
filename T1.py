def calculate(expression: str) -> str:
    operators = ["+", "-", "*", "/"]
    operator = None
    for op in operators:
        if op in expression:
            operator = op
            break

    if operator is None:
        raise ValueError("Недопустимая операция. Допустимые операции: +, -, *, /")

    try:
        parts = expression.split(operator)
        if len(parts) != 2:
            raise ValueError("Некорректный формат ввода. Ожидается выражение вида 'a + b'")

        num1 = int(parts[0].strip())
        num2 = int(parts[1].strip())

        if not (1 <= num1 <= 10 and 1 <= num2 <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно.")

    except ValueError as e:
        raise ValueError(f"Ошибка при разборе чисел: {e}")
    except Exception:
        raise ValueError("Некорректный формат чисел.")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ValueError("Деление на ноль!")
        result = num1 // num2
    else:
        raise ValueError("Недопустимая операция.")

    return str(result)


def main():
    """
    Основная функция консольного калькулятора.
    """
    while True:
        try:
            input_str = input("Введите арифметическое выражение (например, 5 + 3): ")
            if input_str.lower() == "exit":
                break
            result = calculate(input_str)
            print("Результат:", result)
        except ValueError as e:
            print("Ошибка:", e)
            break
        except KeyboardInterrupt:
            print("\nВыход из программы.")
            break


if __name__ == "__main__":
    main()