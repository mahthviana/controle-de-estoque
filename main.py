# FAZER UM CONTROLE DE ESTOQUE
# - ADICIONAR NOVO PRODUTO
# - VER TODOS OS PRODUTOS CADASTRADOS
# - EXCLUIR UM PRODUTO CADASTRADO
# PRODUTO:
#   - NOME, QUANTIDADE, PREÇO


from functions import *

listaProdutos = []

while True:
    menu = int(input("""
        --- Menu ---
    1 - Adicionar Produto
    2 - Ver Podutos
    3 - Excluir Produto
    4 - Editar Produto
    0 - fechar programa
                    
    """))
    
    match menu:
        case 1:
            adicionarProduto()
        case 2:
            print(verProdutos())
        case 3:
            excluirProduto()
        case 4:
            editarProduto()
        case 0:
            break
        case _:
            print("Opção Inválida")

print("Programa encerrado")