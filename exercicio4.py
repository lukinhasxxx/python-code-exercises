# porcental de cada estado no total

# faturamentos mensais por estado
faturamento_por_estado = {
    "São Paulo": 67836.43,
    "Rio de Janeiro": 36678.66,
    "Minas Gerais": 29229.88,
    "Espírito Santo": 27165.48,
    "Demais Estados": 19849.53
}
def porcentagem_faturamento():
    # calcula o total faturado
    total_faturado = sum(faturamento_por_estado.values())

    print("\nOs valores em porcentagem de cada estado são:\n")

    # calcula e imprime a porcentagem de cada estado em relação ao total
    for estado in faturamento_por_estado:
        faturamento = faturamento_por_estado[estado]
        porcentagem_individual = (faturamento / total_faturado) * 100
        print(f"{estado}: {porcentagem_individual:.2f}%")
exibe_porcentagem = porcentagem_faturamento()