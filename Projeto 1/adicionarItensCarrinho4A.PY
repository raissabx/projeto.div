import os
# Adicionar itens
# Remover itens
# Ver itens do carrinho


produtos2 = [{'codigo': 1, 'nome': 'Jenipapo', 'preco': 25,
    'codigo': 2, 'nome': 'Lichia', 'preco': 28,
    'codigo': 3, 'nome': 'Pitaya', 'preco': 30,
    'codigo': 4, 'nome': 'Kiwi', 'preco': 24,
    'codigo': 5, 'nome': 'Goiaba', 'preco': 12,
    'codigo': 6, 'nome': 'Pitanga', 'preco': 14,
    'codigo': 7, 'nome': 'Café', 'preco': 20}]

#dicionário vazio do carrinho

carrinho = {}

opcao = 0
flag_item_4A = True


while flag_item_4A == True:
   
    os.system('cls')
    print('===Carrinho de Compras=== \n')
    print('1 - Adicionar Item')
    print('2 - Remover Item')
    print('3 - Ver itens do carrinho')
    opcao = int(input('Digite a opção: '))
    
       
    if opcao == 1:
        produto = input('Digite o nome do produto: ').title()
        quantidade = int(input('Digite quantidade: '))
        carrinho[produto] = quantidade
        flag_item_4A = False
        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
        if menu == 'S':
           flag_item_4A = True
        
        
    if opcao == 2:
        print(carrinho)
        produto = input('Digite o nome do produto: ').title()
        carrinho.pop(produto)
        for key, value in carrinho.items():
           print(key, ' : ', carrinho[key])
        flag_item_4A = False
        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
        if menu == 'S':
            flag_item_4A = True

    
    if opcao == 3:
        for key, value in carrinho.items():
           print(key, ' : ', carrinho[key])
        flag_item_4A = False
        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
        if menu == 'S':
            flag_item_4A = True
    
   
                
        
       
                
            
        
    



