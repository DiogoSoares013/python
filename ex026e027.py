#encontrando coisas especificas na str
'''txt = str(input('Digite um texto ')).strip().upper()
print(f'A letra A aparece {txt.count('A')} vezes no texto.')
print(f'A primeira letra A apareceu na posicao {txt.find('A')+1}')
print(f'A ultima letra A apareceu em {txt.rfind('A')+1}')'''
#dando o primeiro e ultimo nome
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito Prazer!')
print(f'Seu primeiro nome: {nome[-1]}')
print(f'E seu ultimo nome: {nome[len(nome)-1]}') #nao entendi o por que do -1
#testando
'''nome = ['banana', 'ovo', 'pao']
print(f'{len(nome)}') #por que nao ta contando a lista?
print(type(nome))'''