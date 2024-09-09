#inverter a string

def inverter_string():
    # pega o valor  digitado
    valor_digitado=str(input("diga uma palavra ou frase para inverter\n"))
    lista = [] # começa a lista vazia
    for letra in valor_digitado:
        lista.append(letra)

    #pega o tamanho da lista e tira um pois em python indice começa em 0
    contador = len(lista)-1
    print(f"a palavra/frase invertida fica assim: \n")
    while contador >=0:
        # print começando do final do indice e descendo, ou seja, invertido
        print(lista[contador],end='') # o end='' não quebra a linha
        contador-=1
chamar_inversor=inverter_string()