def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("Valor sacado!")
        print("Retire seu dinheiro na boca do caixa.")

    print("Obrigado por ser nosso cliente!\nTenha um Bom Dia!!!")
    
def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)