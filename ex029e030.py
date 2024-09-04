velocidade = float(input('Qual a velocidade do carro? '))
if velocidade >80:
    print(f'MULTADO! Voce exedeu o limite de velocidade que e de 80km/h \n Voce deve pagar uma multa de R${:2.float(velocidade-80)*7}')
else:
    print(f'Andando a {velocidade} voce esta dentro do limite de velocidade! prossiga normalmente')
