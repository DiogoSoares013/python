#exercicio 22
nome = str(input('Diga seu nome completo: ')).strip()
print('\nCarregando... \n')
print(f'Seu nome em maiusculo fica: {nome.upper()}\n')
print(f'Seu nome em minusculo fica: {nome.lower()}\n')
print(f'Seu nome tem ao todo {len(nome)-nome.count(' ')} letras \n')
print(f'Seu primeiro nome tem {nome.find(' ')} letras\n')
separa = nome.split()
print(f'E seu segundo nome tem {len(separa[1])} letras\n') #forma mais facil de entender e realizar o processo
