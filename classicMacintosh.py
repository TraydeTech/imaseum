''''
CRIADO POR JEFFERSON TRAYDE
DATA DA CRIAÇÃO 23-05-20023
SISTEMA PARA IMUSEUM
'''

def cadastrarClassicMacintosh():
    modelo = input("Digite o modelo: ")
    anoDeFabricacao = input("Digite ano de fabrição: ")
    numeroDeSerie = input("Digite o número de serie: ")
    cor = input("Digite a cor: " )
    osOriginal = input("Digite qual sistema esta instalado: ")
    estado = input("Esta funcionando S/N: ")
    classicMacintosh = {"modelo": modelo, "anoDeFabricacao": anoDeFabricacao, "numeroDeSerie": numeroDeSerie, "cor": cor,
             "osOriginal": osOriginal,  "estado" : estado}
    classicMacintosh.append(classicMacintosh)
    print("Cadastrado com sucesso!")