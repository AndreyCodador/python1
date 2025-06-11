# EXIGÊNCIA DE CÓDIGO 2 de 7
def escolha_servico():
    while True:
        print("\nEntre com o tipo de serviço desejado")
        print("DIG - Digitalização")
        print("ICO - Impressão Colorida")
        print("IPB - Impressão Preto e Branco")
        print("FOT - Fotocópia")
        servico = input(">>").lower()

        if servico == "dig":
            return 1.10  # valor por página
        elif servico == "ico":
            return 1.00
        elif servico == "ipb":
            return 0.40
        elif servico == "fot":
            return 0.20
        else:
            print("Escolha inválida, entre com o tipo do serviço novamente")  # SAÍDA DE CONSOLE 2 de 4


# EXIGÊNCIA DE CÓDIGO 3 de 7
def num_pagina():
    while True:
        try:
            paginas = int(input("Entre com o número de páginas: "))
            if paginas > 20000:
                print("Não aceitamos tantas páginas de uma vez.")  # SAÍDA DE CONSOLE 3 de 4
                continue
            # Cálculo de desconto por quantidade de páginas
            if paginas < 20:
                return paginas
            elif paginas < 200:
                return paginas * 0.85  # 15% de desconto
            elif paginas < 2000:
                return paginas * 0.80  # 20% de desconto
            else:
                return paginas * 0.75  # 25% de desconto
        except ValueError:
            print("Por favor, entre com um número válido de páginas.")


# EXIGÊNCIA DE CÓDIGO 4 de 7
def servico_extra():
    while True:
        print("\nDeseja adicionar algum serviço?")
        print("1 - Encadernação Simples - R$ 15.00")
        print("2 - Encadernação Capa Dura - R$ 40.00")
        print("0 - Não desejo mais nada")
        opcao = input(">>")
        if opcao == "1":
            return 15.00
        elif opcao == "2":
            return 40.00
        elif opcao == "0":
            return 0.00
        else:
            print("Opção inválida. Tente novamente.")


# EXIGÊNCIA DE CÓDIGO 1 de 7 e SAÍDA DE CONSOLE 1 de 4
print("Bem vindo à Copiadora de Andrey Aguiar!")

# Chamada das funções
valor_servico = escolha_servico()
num_paginas_com_desconto = num_pagina()
valor_extra = servico_extra()

# EXIGÊNCIA DE CÓDIGO 5 de 7 (total fora das funções)
total = valor_servico * num_paginas_com_desconto + valor_extra

# Impressão final com detalhes do cálculo — SAÍDA DE CONSOLE 4 de 4
print(f"\nTotal: R$ {total:.2f} (serviço: {valor_servico:.2f} * páginas: {num_paginas_com_desconto:.0f} + extra: {valor_extra:.2f})")

# EXIGÊNCIA DE CÓDIGO 6 de 7: uso de try/except já incluído em num_pagina()
# EXIGÊNCIA DE CÓDIGO 7 de 7: comentários incluídos em todo o código
