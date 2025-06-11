def fazer_pedidos():
    
    print("\nBem-vindo à Loja de Gelados de Andrey Aguiar!")
    print("------------------Cardápio------------------")
    print("| Tamanho | Cupuaçu (CP) | Açaí (AC) |")
    print("|   P     | R$  9.00     | R$ 11.00  |")
    print("|   M     | R$ 14.00     | R$ 16.00  |")
    print("|   G     | R$ 18.00     | R$ 20.00  |")
    print("--------------------------------------------")

    
    precos = {
        "CP": {"P": 9.0, "M": 14.0, "G": 18.0},
        "AC": {"P": 11.0, "M": 16.0, "G": 20.0}
    }

    total = 0.0  

    while True:
        
        sabor = input("Entre com o sabor desejado (CP/AC): ").upper()
        if sabor != "CP" and sabor != "AC":
            print("Sabor inválido. Tente novamente")  
            continue  

        
        tamanho = input("Entre com o tamanho desejado (P/M/G): ").upper()
        if tamanho not in ["P", "M", "G"]:
            print("Tamanho inválido. Tente novamente")  
            continue

        
        if sabor == "CP":
            if tamanho == "P":
                preco = precos["CP"]["P"]
            elif tamanho == "M":
                preco = precos["CP"]["M"]
            else:
                preco = precos["CP"]["G"]
            print(f"Você pediu um Cupuaçu no tamanho {tamanho}: R$ {preco:.2f}")
        elif sabor == "AC":
            if tamanho == "P":
                preco = precos["AC"]["P"]
            elif tamanho == "M":
                preco = precos["AC"]["M"]
            else:
                preco = precos["AC"]["G"]
            print(f"Você pediu um Açaí no tamanho {tamanho}: R$ {preco:.2f}")

        total += preco  

        
        mais = input("Deseja mais alguma coisa? (S/N): ").upper()
        if mais != "S":
            break  

    
    print(f"\nO valor total a ser pago: R$ {total:.2f}")
    print("Obrigado pela preferência!\n")


while True:
    fazer_pedidos()

    
    while True:
        reiniciar = input("Deseja iniciar um novo pedido? (S/N): ").upper()
        if reiniciar == "S":
            break  
        elif reiniciar == "N":
            print("Obrigado por usar a Loja de Gelados de Adnrey Aguiar!")  
            exit()  
        else:
            print("Resposta inválida. Por favor, digite S para sim ou N para não.")  
