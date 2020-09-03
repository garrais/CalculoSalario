import time
nome= input('Primeiramente qual seu nome?: ')
print('Olá {} é um prazer conhece-lo\n'.format(nome))
print('''Eu fui desenvolvida para calcular a porcentagem de aumento do seu salario,
portanto minhas funções são baseadas em calculos precisos,
caso seja necessario, acompanhe os resultados junto a uma calculadora utilizando a seguinte conta:
seu salario*porcentagem de aumento(ex:10) dividido por 100\n''')
salario = int(input('Agora Digite seu Salario: '))
percentual = int(input('Digite o percentual de Aumento: '))
aumento = int(salario*percentual/100)
salario = int(salario+aumento)
print('O Valor do aumento é: ',aumento ,'O Salario atualizado é: ', salario)
print('O Valor estava correto?')
input('Sim ou Nao?: ')
sim=print('Obrigado por Testar!')
nao=print('Por favor, envie seu Feedback pro desenvolvedor Garrais')
time.sleep(30)