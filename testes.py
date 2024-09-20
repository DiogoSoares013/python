
# regra de 3 testando COTAS DE INVESTIMENTO
print('UNIDADE!! \n')
v1 = float(input('Digite o valor da cota '))
r1 = float(input('Digite quanto que recebe a unidade por essa cota '))
vx = float(input('Digite quantas cotas voce quer testar '))
v1C = vx * v1

resx = (r1 * v1C)/v1 

print(f'\nO resultado da regra deu {resx} \nVoce iria gastar {v1C} para receber aquela quantia\n')
