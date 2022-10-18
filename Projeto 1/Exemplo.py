import os

# Flags liga/desliga para controle da execução do while
flag_menu_vendas=True   
flag_item_4A=False
flag_item_4C=False

while flag_menu_vendas:
    os.system("cls")
    
    print("MENU DE VENDAS")
    print("a. Adição de produtos ao carrinho")
    print("c. Finalização da venda do carrinho")
    print("s. Sair do sistema")
    opção=input("Opção:")
    if opção=="a":
        flag_item_4A=True
        flag_item_4C=False
    elif opção=="c": 
        flag_item_4A=False
        flag_item_4C=True 
    elif opção=="s":
        flag_item_4A=False
        flag_item_4C=False
        flag_menu_vendas=False
    
    while flag_item_4A:
        print("\n*** Adição de produtos ao carrinho *** ")
        print("m. Voltar ao menu Vendas")
        print("s. Sair do sistema")    
        opção=input("Opção: ")
        
        if opção=="m": 
            flag_item_4A=False
            flag_item_4C=False
        elif opção=="s":
            flag_item_4A=False
            flag_item_4C=False
            flag_menu_vendas=False

    while flag_item_4C:
        print("\n*** Finalização da venda do carrinho ***")
        print("m. Voltar ao menu Vendas")
        print("s. Sair do sistema")
        opção=input("Opção: ")
        
        if opção=="m": 
            flag_item_4A=False
            flag_item_4C=False
        elif opção=="s":
            flag_item_4A=False
            flag_item_4C=False
            flag_menu_vendas=False

print("\nP R O G R A M A   E N C E R R A D O\n")