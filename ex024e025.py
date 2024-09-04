cidade = str(input('Em que cidade voce nasceu? ')).strip()
print(f'{cidade[:5]=='Santo'}') # o == serve para saber se a sentença é igual naquele espaço especifico igual

#procurando o nome na string
nome = str(input('qual seu nome completo? ')).strip()
print(f'{'silva' in nome.lower()}')