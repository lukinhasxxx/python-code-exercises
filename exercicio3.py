#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
import requests
import json

# valores em json passados
url = requests.get('https://drive.google.com/uc?id=1qXvCPjEL4jerElN-hnScoKkEVmSQ8A2L')

# inicializando lista vazia 

valoresJson = url.json()
def calcula_faturamento(valoresJson):

    # inicializando lista vazia 
    itens_para_media=[]
    
    #iteração sobre as chaves para depois buscar especificamente os valores em ''valor''
    for itens in valoresJson:
        valores=itens["valor"]
        if valores is not None and valores != 0:
            itens_para_media.append(valores)

    # menor valor de faturamento em um dia do mês
    print(f"O menor faturamento do mês foi: R$ {(min(itens_para_media)):.2f}\n")

    # maior valor de faturamento em um dia do mês
    print(f"O maior faturamento do mês foi: R$ {(max(itens_para_media)):.2f}\n")
    
    # media mensal
    mediaMensal=sum(itens_para_media)/len(itens_para_media)
    print(f"a media mensal de faturamento é de R${mediaMensal:.2f}")
          
    # contador e loop para ver quantos dias são acima da média
    dias_acima_da_media = 0
    for mediaDiaria in itens_para_media:
        if mediaDiaria > mediaMensal:
            dias_acima_da_media+=1
    print(f"Neste mês {dias_acima_da_media} dias foram acima da média mensal\n")
    
# executando a função acima    
executaCalculo=calcula_faturamento(valoresJson)