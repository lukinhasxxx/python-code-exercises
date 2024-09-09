
def pertence_a_fibonacci(numero):
    # iniciando os dois valores iniciais do fibonacci para começar de forma certa
    valor_anterior = 0
    valor_atual = 1
    
    # caso o numero seja 0 ou 1, ele pertence a sequência
    if numero == valor_anterior or numero == valor_atual:
        return True
    
    # gerar a sequencia de fibonacci até o valor atual ser maior ou igual ao número
    while valor_atual < numero:
        # atualiza os valores para o próximo numero na sequencia
        proximo_valor = valor_anterior + valor_atual
        valor_anterior = valor_atual
        valor_atual = proximo_valor
    
    # verifica se o numero informado é igual ao valor atual
    return numero == valor_atual

# solicita ao usuario que informe um numero
numero_informado = int(input("digite um numero para verificar se pertence à sequência de fibonacci: "))

# verificar se o numero pertence à sequência e exibir a mensagem correspondente
if pertence_a_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence a sequencia de fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequencia de fibonacci.")
