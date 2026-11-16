import re

def shunting_yard(expression: str) -> str:

    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }
    tokens = re.findall(r'\d+(?:\.\d+)?|[+\-*/()]', expression)
    
    output = []
    stack = []

    for token in tokens:
        if re.match(r'^\d+(?:\.\d+)?$', token):
            output.append(token)
        
        
        elif token in precedence:
            while (stack and stack[-1] != '(' and 
                   precedence.get(stack[-1], 0) >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        
        
        elif token == '(':
            stack.append(token)
        
        
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                raise ValueError("Несогласованные скобки [пропущена '(']")
            stack.pop()

    
    while stack:
        if stack[-1] == '(':
            raise ValueError("Несогласованные скобки [пропущена ')']")
        output.append(stack.pop())

    return " ".join(output)

print(shunting_yard(str(input)))