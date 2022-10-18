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


carrinho = {}

opcao = 0
flag_item_4A = True


while flag_item_4A:
   
    os.system('cls')
    print('===Carrinho de Compras=== \n')
    print('1 - Adicionar Item')
    print('2 - Remover Item')
    print('3 - Ver itens do carrinho')
    opcao = int(input('Digite a opção: '))
    
       
    if opcao == 1:
        print(produtos2)
        id = int(input('Digite o código do produto: '))
        quantidade = int(input('Digite quantidade: '))
        carrinho.update({id:quantidade})
        flag_item_4A = False
        menu = input('Deseja voltar ao menu do carrinho de compras? S ou N: ').title()
        if menu == 'S':
           flag_item_4A = True
        
        
    if opcao == 2:
        print(carrinho)
        id = input('Digite o código do produto: ')
        remover = carrinho.pop(id)
        print(carrinho)
        #for key, value in carrinho.items():
        #   print(key, ' : ', carrinho[key])
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
    
   
               
        
       
                
            
        
    



