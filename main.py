alphabet = set("1234567890.+-*/()")

#ANÁLISE LÉXICA
def scanner(expression):
    expression = expression.replace(" ", "")
    token_list = []
    number = ""
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                if '.' in number:
                    #print("Número decimal: " + number)
                    token_list.append(float(number))
                else:
                    #print("Número inteiro: " + number)
                    token_list.append(int(number))
                number = ""
            if char == '+':
                #print("Operador: " + char)
                token_list.append('OPSOMA')
            elif char == '-':
                #print("Operador: " + char)
                token_list.append('OPSUB')
            elif char == '*':
                #print("Operador: " + char)
                token_list.append('OPMUL')
            elif char == '/':
                #print("Operador: " + char)
                token_list.append('OPDIV')
            elif char == '(':
                #print("Parêntese: " + char)
                token_list.append('AP')
            elif char == ')':
                #print("Parêntese: " + char)
                token_list.append('FP')
            else:
                raise Exception("Caractere inválido na expressão: " + char)
    if number:
        if '.' in number:
            token_list.append(float(number))
        else:
            token_list.append(int(number))
    #print("ANÁLISE LÉXICA 🆗! Não há caracteres inválidos.")
    return token_list


# TROCA DE NOTAÇÃO PARA NOTAÇÃO POLONESA REVERSA NPR
def infix_para_npr(token_list):
    precedence = {'OPSOMA': 1, 'OPSUB': 1, 'OPMUL': 2, 'OPDIV': 2}
    output = []
    operator_stack = []
    for token in token_list:
        if type(token) in [int, float]:
            output.append(token)
        elif token in ['OPSOMA', 'OPSUB', 'OPMUL', 'OPDIV']:
            while operator_stack and operator_stack[-1] != 'AP' and precedence[token] <= precedence[operator_stack[-1]]:
                output.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == 'AP':
            operator_stack.append(token)
        elif token == 'FP':
            try:
                while operator_stack[-1] != 'AP':
                    output.append(operator_stack.pop())
                operator_stack.pop()
            except IndexError:
                raise Exception("A expressão é inválida. Parêntese de abertura não encontrado.")
    while operator_stack:
        if operator_stack[-1] == 'AP':
            raise Exception("A expressão é inválida. Parêntese de fechamento não encontrado.")
        output.append(operator_stack.pop())
    return output


def parser(output):
    stack = []
    for token in output:
        if type(token) in [int, float]:
            stack.append(token)
        elif token in ['OPSOMA', 'OPSUB', 'OPMUL', 'OPDIV']:
            try:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == 'OPSOMA':
                    stack.append(num1 + num2)
                elif token == 'OPSUB':
                    stack.append(num1 - num2)
                elif token == 'OPMUL':
                    stack.append(num1 * num2)
                elif token == 'OPDIV':
                    try:
                        stack.append(num1 / num2)
                    except ZeroDivisionError:
                        raise Exception("A expressão é inválida. Há uma divisão por zero.")
            except IndexError:
                raise Exception("A expressão é inválida. Verifique se os operadores estão corretos.")
    #print("ANÁLISE SINTÁTICA 🆗! Não há erros de sintaxe.")
    return stack.pop()


def calculator(expression):
    return float(f"{parser(infix_para_npr(scanner(expression))):.4f}")