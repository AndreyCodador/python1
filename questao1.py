
print("Seja bem-vindo loja do Andrey de Lima Aguiar.\n")

valor_str = input("Digite o valor unitário do produto: R$ ")
valor_unitario = float(valor_str.replace(",", "."))  # Troca vírgula por ponto


quantidade = int(input("Digite a quantidade do produto: "))


valor_total_sem_desconto = valor_unitario * quantidade


if valor_total_sem_desconto < 2500:
    desconto = 0
elif valor_total_sem_desconto < 6000:
    desconto = 0.04  
elif valor_total_sem_desconto < 10000:
    desconto = 0.07  
else:
    desconto = 0.11  


valor_com_desconto = valor_total_sem_desconto * (1 - desconto)


print("\nMuito obrigado por usar o sistema. Andrey Aguiar Agradece!")

print("Aqui estão os detalhes do seu pedido:")
print(f"Valor unitário: R$ {valor_unitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"\nValor total sem desconto: R$ {valor_total_sem_desconto:.2f}")


if desconto > 0:
    print(f"Desconto aplicado: {int(desconto * 100)}%")
    print(f"Valor total com desconto: R$ {valor_com_desconto:.2f}")
else:
    print("Nenhum desconto aplicado.")
