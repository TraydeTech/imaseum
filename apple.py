''''
CRIADO POR JEFFERSON TRAYDE
DATA DA CRIAÇÃO 23-05-20023
SISTEMA PARA IMUSEUM
'''


def cadastrarApple():
    modelo = input("Digite o modelo: ")
    anoDeFabricacao = input("Digite ano de fabrição: ")
    numeroDeSerie = input("Digite o número de serie: ")
    cor = input("Digite a cor: " )
    osOriginal = input("Digite qual sistema esta instalado: ")
    estado = input("Esta funcionando S/N: ")
    apple = {"modelo": modelo, "anoDeFabricacao": anoDeFabricacao, "numeroDeSerie": numeroDeSerie, "cor": cor,
             "osOriginal": osOriginal,  "estado" : estado}
    apple.append(apple)
    print("Cliente cadastrado com sucesso!")