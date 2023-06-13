''' Caulculadora while'''

'''
Nessa calculadora usamos o input para pedir os numeros e o operador
usamos tambem o none, caso numero_valido seja igual a nome escrever que a quantidade
de numeros excedeu, se quantidade de operadores for 2 escrever 
digite apenas um operador ( para isso usamos o len), e usamos o if not in para
caso seja escrito um operador que não esta na lista
depois foi criado um novo if, elif para realizar a operação de cada numero
e por fim um break onde quando fosse digitado S ou Sair ele quebraria o loop

'''
while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são invalidos.')
        continue

    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. confira o resultado abaixo')
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} =',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)
        
    else:
        print('Nunca deve se chegar aqui kkkkkkkkkkk.')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
  










