
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Нельзя делить на ноль"
    return a / b

def main():
    print("📱 Простой калькулятор на Python")
    print("Выберите операцию:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")

    op = input("Введите номер операции (1/2/3/4): ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if op == '1':
        print("Результат:", add(a, b))
    elif op == '2':
        print("Результат:", subtract(a, b))
    elif op == '3':
        print("Результат:", multiply(a, b))
    elif op == '4':
        print("Результат:", divide(a, b))
    else:
        print("❌ Неверный выбор")

if __name__ == "__main__":
    main()
