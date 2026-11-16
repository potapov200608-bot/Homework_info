def eval_rpn(expression: str):

    tokens = expression.strip().split()
    if not tokens:
        return 
    
    stack = []
    


    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '//': lambda a, b: a // b,
        '%': lambda a, b: a % b,
        '**': lambda a, b: a ** b,
        '^': lambda a, b: a ** b
    }

    for token in tokens:

        try:
            number = float(token)
            stack.append(number)
            continue
        except ValueError:
            pass

        if token in operators:

            if len(stack) < 2:
                return "Выражение составлено некорректно (недостаточно операндов)"
            
            b = stack.pop()
            a = stack.pop()
            
            if token in ('/', '//', '%') and b == 0:
                return "Деление на ноль"
            
            try:
                result = operators[token](a, b)
                stack.append(result)
            except Exception as e:
                return f"Ошибка при вычислении: {e}"
        else:
            return f"Выражение составлено некорректно"

    if len(stack) != 1:
        return "Выражение составлено некорректно"

    res = stack[0]
    return int(res) if res.is_integer() else res

print(eval_rpn(str(input())))