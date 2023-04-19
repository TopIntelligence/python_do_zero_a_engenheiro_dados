# 01_Introducao_Python
# Verifica versão
python --version

# String
"Olá Mundo! Estou na aula de Python!"
print("Bem vindo ao Top Intelligence Academy!")

# Salve o arquivo e acesse o diretório via prompt e digite
python nomedoseuarquivo.py

# Comentário de uma linha

"""Comentário 
de 
Múltiplas linhas"""

''' Anotações 
de múltiplas
Linhas'''

# Operação matemática Básica
4+5
2*3
6/2
2.5 + 3.4
4 + 5 * 2
(4+5) * 2

# Limpando Terminal Python Shell
import os
from time import sleep

# Imprimindo textos
print("Aula de Python")
print("Limpar tela após 5 segundos")

# Aguardando 5 segundos
sleep(5)

# Limpando a tela
os.system('cls')

# Outra possibilidade - incluir 100 linhas em branco
print ("\n" * 100) 

# Outra possibilidade via função
def cls():
    os.system("cls")
# enter    
cls()

# Utilizando lambda
clear = lambda : os.system('cls')
clear()

# Variáveis
a = "Top Intelligence"
a
type(a)
a = 3
a
type(a)
b = 4*2
b
c = a + b
a = 5
c
c = a + b
c
A
user_age = 35
user_age

# Entradas de Informação pelo usuário
user_name = input("Qual é o seu nome? ")
user_age = input("Qual a sua idade? ")
type(user_age)
print("Olá " + user_name + ", você tem " + user_age + "anos.")

# Estrutura condicional - "SE"
if int(user_age) > 18:
  print("É maior de 18")

# Operações com entradas
a = int(input("Primeiro Número: "))
b = int(input("Segundo Número: "))
sum = a + b

# Converte variável numérica em string para concatenar
str(a) + " + " + str(b) + " = " + str(sum)

# Obtém a quantidade de caracteres da sentença
len("Olá Mundo! Estou na aula de Python!")

# Listas
empresa= ['Top', 'Intelligence', 'Academy']

len(empresa)

# Média de uma lista
number_list = [4.4, 5.5, 6.6, 7.7]
media = sum(number_list) / len(number_list)
media