import random 
import time
print('===== WELCOME TO GAME IN PYTHON ===== \n')
numero = int(input('Digite um numero de 0 a 5 para ver se voce acertou '))
n = [0, 1, 2, 3, 4, 5] #da pra fazer com o randint para randomizar um numero inteiro randint(0, 5) caberia um nesse contexto
r = random.choice(n)
print('Carregando...')
time.sleep(3)
if r == numero:
    print(f'\n Voce escolheu {numero} e o computador {r} \n PARABENS VOCE ACERTOU')
else:
    print(f'Voce perdeu ;-; o computador escolheu {r}')

