# calcula soma dos numeros de 1 até o valor do índice (que é fixo)

INDICE = 13 #constante, por isso em caps
def calcula_soma(INDICE):
    soma = 0
    k = 0
    # loop atualizando valor de K e da Soma
    while k < INDICE:
        k=k+1
        soma=soma+k
    return soma
resultado_soma=calcula_soma(INDICE)
print(f"O resultado da soma deu: {resultado_soma}")
