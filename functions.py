listaProdutos = []

def adicionarProduto():
    nome = input("Digite o nome do produto: ")
    qntd = int(input("Quantidade de produtos: "))
    preco = float(input("Preço do produto: "))

    dadosProduto = {
        "nome":nome,
        "qntd":qntd,
        "preço":preco
    }

    listaProdutos.append(dadosProduto)
    print("Produto cadastrado com sucesso!")

def verProdutos():
    lista = ""
    for produtoDaVez in listaProdutos:
        lista += f"""
            Produto: {produtoDaVez['nome']}
            quantidade: {produtoDaVez['qntd']}
            Preço: R${produtoDaVez['preço']}
    """
    return lista

def excluirProduto():
    produto = input("Digite o nome de um produto cadastrado que deseja ecluir: ")

    for produtoDaVez in listaProdutos:
        if produtoDaVez["nome"].lower() == produto.lower():
            listaProdutos.remove(produtoDaVez)
            print(f"Produto {produtoDaVez['nome']} foi removido com sucesso")
            produtoEncontrado = True

        if not produtoEncontrado:
            print(f"O produto {produtoDaVez} não foi encontrado")

def editarProduto(): 
    produto = input("Qual produto você deseja editar: ")
    for produtoDaVez in listaProdutos:
        if produtoDaVez["nome"].lower() == produto:
            menu = input("""
        O que você deseja editar:
                1 - Nome
                2 - Quantidade no estoque
                3 - Preço
    """)
            match menu:
                case "1":
                    novoNome = input("Digite o novo nome do produto: ")
                    produtoDaVez["nome"] = novoNome
                case "2":
                    novaQuantidade = int(input("DIgite a nova quantidade: "))
                    produtoDaVez["qntd"] = novaQuantidade
                case "3":
                    novoPreco = float(input("Digite o novo preço: "))
                    produtoDaVez["preco"] = novoPreco
            produtoEncontrado = True
                    
    if not produtoEncontrado:
        print("Produto não encontrado..")