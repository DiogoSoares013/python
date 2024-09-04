import time, random
print('Ola usuário! oque vamos fazer hoje?\n')
print('Aqui vai uma lista do que pode ser feito \n 1-Calcular descontos \n 2-Calcular triangulo \n 3-Sortear')
atividade = int(input('Digite o número da atividade que deseja fazer '))
if atividade == 1:
    print('Carregando...')
    import time
    time.sleep(3)
    desconto = int(input('De quantos porcento estamos falando? '))
    valorproduto = float(input('Agora digite o valor do produto para saber o desconto '))
    print(f'\n Perfeito! o produto que estava custando R${valorproduto} agora custa R${valorproduto-(valorproduto*desconto/100)}')
if atividade == 2:
    import math
    print('Carregando...')
    time.sleep(3)
    print('\n Ok agora iremos descobrir o seno, cosseno e tangente do triangulo')
    print('\n ATENÇÃO!! Caso nao saiba um dos valores abaixo apenas digite 0')
    seno = int(input('Digite o valor do seno '))
    cosseno = int(input('Digite o valor do cosseno '))
    tangente = int(input('Digite o valor da tangente '))
    print(f'Entendi! os valores foram, respectivamente, {seno}, {cosseno}, {tangente}')
    print(f'E o resultado para cada um deles será, respectivamente, de: \n {math.sin(seno)} \n {math.cos(cosseno)} \n {math.tan(tangente)} ')
if atividade == 3:
        print('Ok vamos entender oque iremos sortear')
        sorteio = int(input('\n Se iremos sortear numeros digite 1 \n Ou e iremos sortear pessoas,objetos ou qualquer tipo de coisa digite 2 '))
        if sorteio == 1:
             valor1 = int(input('Digite o valor inicial: '))
             valor2 = int(input('Digite o segundo valor: '))
             print(f'Sorteando de {valor1} a {valor2} o numero saiu: {random.randint(valor1,valor2)}') #como que faz pra pessoa escolher de x a x?
        if sorteio == 2:
            pessoas = str(input('Digite as pessoas envolvidas a serem sorteadas ')).strip().replace(',','').split()
            print(f'O escolhido foi {random.choice(pessoas)}')

        
