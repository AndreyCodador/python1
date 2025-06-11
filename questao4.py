
print("Bem-vindo à Livraria do Andrey Aguiar")

livros = []
id_atual = 1

while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1 - Cadastrar Livro")
    print("2 - Consultar Livro(s)")
    print("3 - Remover Livro")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- CADASTRAR LIVRO ---")
        nome = input("Digite o nome do livro: ")
        autor = input("Digite o autor do livro: ")
        editora = input("Digite a editora do livro: ")

        livro = {
            "id": id_atual,
            "nome": nome,
            "autor": autor,
            "editora": editora
        }
        livros.append(livro)
        print("Livro cadastrado com sucesso!")
        id_atual += 1

    elif opcao == "2":
        print("\n--- CONSULTAR LIVROS ---")
        print("1 - Ver todos")
        print("2 - Buscar por ID")
        print("3 - Buscar por autor")
        print("4 - Voltar")
        escolha = input("Opção: ")

        if escolha == "1":
            for l in livros:
                print(f"\nID: {l['id']}")
                print(f"Nome: {l['nome']}")
                print(f"Autor: {l['autor']}")
                print(f"Editora: {l['editora']}")
        elif escolha == "2":
            try:
                busca_id = int(input("Digite o ID do livro: "))
                encontrado = False
                for l in livros:
                    if l["id"] == busca_id:
                        print(f"\nID: {l['id']}")
                        print(f"Nome: {l['nome']}")
                        print(f"Autor: {l['autor']}")
                        print(f"Editora: {l['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro não encontrado.")
            except:
                print("ID inválido.")
        elif escolha == "3":
            autor_nome = input("Digite o nome do autor: ")
            achou = False
            for l in livros:
                if l["autor"].lower() == autor_nome.lower():
                    print(f"\nID: {l['id']}")
                    print(f"Nome: {l['nome']}")
                    print(f"Autor: {l['autor']}")
                    print(f"Editora: {l['editora']}")
                    achou = True
            if not achou:
                print("Nenhum livro encontrado com esse autor.")
        elif escolha == "4":
            continue
        else:
            print("Opção inválida.")

    elif opcao == "3":
        try:
            remover_id = int(input("Digite o ID do livro a remover: "))
            removido = False
            for l in livros:
                if l["id"] == remover_id:
                    livros.remove(l)
                    print("Livro removido.")
                    removido = True
                    break
            if not removido:
                print("Livro não encontrado.")
        except:
            print("Digite um número válido.")

    elif opcao == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")
