def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isspace():
            i += 1
            continue

        if char.isdigit() or char == '.':
            num_str = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            tokens.append(num_str)
        elif char in "+-*/()":
            tokens.append(char)
            i += 1
        else:
            raise ValueError({char})
    return tokens

def get_precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

def to_rpn(expression):

    tokens = tokenize(expression)
    output_queue = []
    operator_stack = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            output_queue.append(token)
        elif token in "+-*/":
            while (operator_stack and operator_stack[-1] != '(' and
                   get_precedence(operator_stack[-1]) >= get_precedence(token)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if not operator_stack:
                raise ValueError()
            operator_stack.pop()

    while operator_stack:
        op = operator_stack.pop()
        if op == '(':
            raise ValueError()
        output_queue.append(op)

    return " ".join(output_queue)

def to_lpn(expression):

    tokens = tokenize(expression)

    reversed_tokens = []
    for token in reversed(tokens):
        if token == '(':
            reversed_tokens.append(')')
        elif token == ')':
            reversed_tokens.append('(')
        else:
            reversed_tokens.append(token)
    
    rev_expr = "".join(reversed_tokens)
    output_queue = []
    operator_stack = []

    for token in rev_expr.split():
        pass

    rev_tokens = tokenize(rev_expr)
    for token in rev_tokens:
        if token.replace('.', '', 1).isdigit():
            output_queue.append(token)
        elif token in "+-*/":
  
            while (operator_stack and operator_stack[-1] != '(' and
                   get_precedence(operator_stack[-1]) > get_precedence(token)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return " ".join(reversed(output_queue))


expression = str(input())
print(to_rpn(expression))
print(to_lpn(expression))