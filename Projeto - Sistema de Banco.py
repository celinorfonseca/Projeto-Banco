#função para obtenção da data
from datetime import datetime

#Classes globais
saldo = 0.0
transacoes = []  # Lista onde serão armazenados os depósitos e saques para o extrato.
saques_realizados = []  # Lista onde serão armazenados os saques realizados no dia.

#Definições das variáveis que serão utilizadas
def depositar(valor):
    global saldo, transacoes
    if valor > 0:
        saldo += valor
        transacoes.append((datetime.now(), f"Depósito: R${valor:.2f}"))
        return f"Depósito de R${valor:.2f} realizado com sucesso (☆^-^☆). Saldo atual: R${saldo:.2f} \($-$)/"
    else:
        return "Operação não realizada. O valor do depósito deve ser positivo. (ノಠ益ಠ)ノ彡┻━┻"

def sacar(valor):
    global saldo, saques_realizados, transacoes
    hoje = datetime.now().date()

   #Parte do código destinada a idetificar a quantidade de saques realizados no dia.
    saques_hoje = [data for data in saques_realizados if data == hoje]

    if len(saques_hoje) >= 3:
        print("Operação não realizada. Você já realizou 3 saques hoje. (ㄒoㄒ)")
    
    elif valor > 500:
        print("Operação não realizada. O valor máximo de saque é R$500,00 por operação. o(╥﹏╥)o")
    
    elif valor > saldo:
        print("Operação não realizada. Saldo insuficiente. (*ﾉωﾉ)")
    
    elif valor <= 0:
        print("Operação não realizada. O valor do saque deve ser positivo. (ノಠ益ಠ)ノ彡┻━┻")
    
    # Saque realizado caso as condições anteriores não se encaixem.
    elif valor > 0:
        saldo -= valor
        saques_realizados.append(hoje)
        transacoes.append((datetime.now(), f"Saque: R${valor:.2f}"))
        print(f"Saque de R${valor:.2f} realizado com sucesso ♥～(‘▽^人). Saldo atual: R${saldo:.2f}")
    else:
        print("Operação falhou! Valor informado é inválido.")

def extrato():
    global saldo, transacoes
    if not transacoes:
        print("Nenhuma transação realizada. (>_<)")
    extrato = "-------- Extrato de transações:---------\n"
    for data, transacao in transacoes:
        extrato += f"{data.strftime('%d/%m/%Y %H:%M:%S')} - {transacao}\n"
    extrato += f"Saldo atual: R${saldo:.2f}\n"
    print(extrato)

# Menu de interação
def menu():
    while True:
        print("\n--- Bem vindo ao meu banco ヾ(^-^)ノ ---")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor do depósito: "))
            print(depositar(valor))
        elif opcao == "2":
            valor = float(input("Digite o valor do saque: "))
            print(sacar(valor))
        elif opcao == "3":
            print(extrato())
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
menu()
