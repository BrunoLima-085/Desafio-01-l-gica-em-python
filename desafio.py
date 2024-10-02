import datetime
import random

def finalexp():
    hragora = datetime.datetime.now()
    hratual = hragora.time()
    hrfinal = datetime.time(23,20)
    return hratual < hrfinal

vendas = []
def cadvenda():
    codvenda = int(input("\nFavor cadastre o código da venda: "))
    cadnome = input("\nNome do cliente: ")
    cadendereço = input("Endereço do cliente: ")
    cadtelefone = int(input("Telefone do cliente: "))

    vendas.append({"nome": cadnome})

def sorteio():
    if vendas:
        vencedor = random.choice(vendas)
        print(f"\nO(a) sortudo(a) é: {vencedor ['nome']}")
    else:
        print("Não há venda. Não houve vencedor(a).")

while finalexp():
    cadvenda()
print("\nFinal do expediente!!!")
sorteio()