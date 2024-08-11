def calcular_valor_maximo(operadores, operandos) -> float:
    resultados = map(lambda op_ab: aplicar_operacao(op_ab[0], op_ab[1][0], op_ab[1][1]), zip(operadores, operandos))
    
    return max(resultados)

def aplicar_operacao(op, a, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else float('inf')
    elif op == '%':
        return a % b if b != 0 else float('inf')
    else:
        raise ValueError(f"Operador desconhecido: {op}")
