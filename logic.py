# logic.py
def evaluate_expression(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"
    except Exception:
        return "Ошибка: некорректное выражение"
