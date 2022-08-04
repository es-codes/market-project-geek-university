from models.produto import Produto
from utils.helper import float_to_str
from time import sleep
from typing import List, Dict

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []

def main() -> None:
    return menu()

def menu() -> None:
    print(f'=============================')
    print(f'========BEM VINDO(A)=========')
    print(f'==========ES SHOP============')
    print(f'=============================')

    sleep(1)

    n = int(input((f'Escolha uma das opções do menu:\n'
        '[1] CADASTRAR UM PRODUTO\n'
        '[2] LISTAR OS PRODUTOS\n'
        '[3] COMPRAR UM PRODUTO\n'
        '[4] VER O CARRINHO\n'
        '[5] FINALIZAR A COMPRA\n'
        '[6] SAIR DO PROGRAMA\n'
        )))

    if n == 1:
        cadastrar()
    elif n == 2:
        listar()
    elif n == 3:
        comprar()
    elif n == 4:
        ver_carrinho()
    elif n == 5:
        finalizar_compra()
    elif n == 6:
        print('Obrigado, volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida!')
        sleep(1)
        menu()
    
    


def cadastrar() -> None:
    print('Cadastro de Produto')
    print('===================')
    
    nome: str = input('Nome: ')
    valor: float = float(input('Valor: '))

    produto: Produto = Produto(nome, valor)

    if len(produtos) > 0:
        for n in produtos:
            if produto.name == n.name:
                print(f'O produto {produto.name} já está cadastrado.')
                sleep(2)
                menu()
            else:
                produtos.append(produto)
                print(f'Produto {produto.name} adicionado com sucesso.')
                sleep(2)
                menu()

    else:
        produtos.append(produto)
        print(f'Produto {produto.name} adicionado com sucesso.')
        sleep(2)
        menu()


def listar() -> None:
    
    if len(produtos) == 0:
        print(f'Ainda nenhum produto foi adicionado ao sistema.')
        sleep(1)
        menu()
    else:
        print('Listagem de produtos')
        print('--------------------')
        for n in produtos:
            print('======================')
            print(n)
            print('======================')
            sleep(1)
    sleep(1)
    menu()


def comprar() -> None:
    if len(produtos) == 0:
        print(f'Ainda nenhum produtos para vender.')
        sleep(1)
        menu()
    else:
        print('Informe o código do produto que deseja adicionar ao carrinho: ')
        print('--------------------------------------------------------------')
        print('================== Produtos Disponíveis ======================')
        
        sleep(1)
        
        for n in produtos:
            print(n)
            print('=====================')
        
        cod = int(input())

        produto: Produto = pega_produto_por_codigo(cod)
        if produto:
            if len(carrinho) == 0:
                carrinho.append({produto: 1})
                print(f'ítem {produto.name} adicionado ao carrinho!')
                sleep(1)
                c = int(input('Deseja continuar comprando? (1 = Sim/0 = Não)'))
                if c:
                    sleep(1)
                    comprar()
                else:
                    sleep(1)
                    menu()

            else:
                for item in carrinho:
                    if item.get(produto):
                        item[produto] = item.get(produto) + 1
                        print(f'O produto {produto.name} agora possui {item.get(produto)} unidades no carrinho.')
                        c = int(input('Deseja continuar comprando? (1 = Sim/0 = Não)'))
                        if c:
                            sleep(1)
                            comprar()
                        else:
                            sleep(1)
                            menu()
                    else:
                        carrinho.append({produto: 1})
                        print(f'O produto {produto.name} foi adicionado ao carrinho.')
                        sleep(1)
                        c = int(input('Deseja continuar comprando? (1 = Sim/0 = Não)'))
                        if c:
                            sleep(1)
                            comprar()
                        else:
                            sleep(1)
                            menu()
        else:
            print(f'Código inválido, tente novamente.')
            sleep(1)
            comprar()        

def ver_carrinho() -> None:
    if len(carrinho) == 0:
        print('O carrinho ainda está vazio.')
        sleep(1)
        menu()
    else:
        print('----------------------')
        print('Produtos no carrinho: ')
        print('----------------------')
        for item in carrinho:
            for produto in item.items():
                print(produto[0])
                print(f'Quantidade: {produto[1]}')
                print('-------------------')
            sleep(1)
    sleep(2)
    menu()      

def finalizar_compra() -> None:
    if len(carrinho) == 0:
        print(f'Você não tem nenhum produto em seu carrinho.')
        sleep(1)
        menu()
    else:
        valor: float = 0
        fatura_total: float = 0
        for item in carrinho:
            for produto in item.items():
                print(produto[0])
                print(f'Quantidade: {produto[1]}')
                valor = produto[0].price * produto[1]
                print(f'Fatura: {float_to_str(valor)}')
                fatura_total += valor
                print('----------------------------')
        print(f'Fatura total: {float_to_str(fatura_total)}')        
        print('Volte sempre!')
        carrinho.clear()
    sleep(3)
    menu()


def pega_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()