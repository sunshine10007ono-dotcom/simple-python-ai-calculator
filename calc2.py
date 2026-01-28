def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def calculator():
    print("Простой калькулятор")
    print("Операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числовое значение!")
            continue

        op = input("Выберите операцию (+, -, *, /) или 'q' для выхода: ")
        if op == 'q':
            print("Выход из программы.")
            break

        if op == '+':
            print("Результат:", add(a, b))
        elif op == '-':
            print("Результат:", subtract(a, b))
        elif op == '*':
            print("Результат:", multiply(a, b))
        elif op == '/':
            print("Результат:", divide(a, b))
        else:
            print("Неизвестная операция. Попробуйте снова.")

if __name__ == "__main__":
    calculator()
