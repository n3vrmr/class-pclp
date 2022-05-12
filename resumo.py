# -*- coding: utf-8 -*-
"""
Created on Thu May 12 18:25:59 2022

@author: Nevermore
"""

# Variáveis simples
a = 27 # variável de tipo inteiro (int)
b = "Vou tirar 10" # variável de tipo texto (str)
c = 36.5 # variável de tipo ponto flutuante (float)
d = True # variável de tipo booleano (bool)

# Estruturas de dados
lista_alunos = ["Gabi", "Caetano", "Thiago",
                "Felipe", "Heloísa", "Larissa"] # lista de nomes, pode conter outros elementos que sejam de outros tipos
alunos_publi = {"Gabi":"balé", "Caetano":True, 
                "Thiago":20, "Felipe":"ataca", 
                "Heloísa":1.8, "Larissa":"Taylor Swift"} # dicionário, nomes são chaves
                                                         # valor é o que vem depois dos dois pontos para cada elemento

# Substituindo o valor de uma lista
lista_alunos[2] = "Tcheba" # substitui o terceiro elemento da lista por "Tcheba"

# Substituindo o valor associado a uma chave em um dicionário
alunos_publi["Caetano"] = False # chave entre colchetes
                                # isso faz com que apareça 'Caetano':False no dicionário

# Laços (loops)
# laço for
for aluno in lista_alunos: # cria uma variável 'aluno' e executa as linhas indentadas abaixo para cada elemento da lista
    print(f"Olá, tudo bem, {aluno}?")
    
# laço while
while d: # executa as linhas indentadas abaixo enquanto a condição for verdadeira
    d = False # quebra o laço infinito
    print("Ufa, não é um laço infinito!")

# Condições if, elif e else
if 1>2: # se a condição for verdadeira, executa as linhas indentadas abaixo (1 é maior que 2?)
    print("Esta linha não será executada, pois a condição não é verdadeira")
elif 2!=2: # se o primeiro if não for verdadeiro, verifica se a condição depois de elif é verdadeira ou não (2 é diferente de 2?)
    print("Esta linha também não será executada")
else: # caso nenhuma condição if ou elif for satisfeita, exceuta as linhas indentadas abaixo
    print("Esta linha será executada")

# Aplicando em um bloco for
for aluno in lista_alunos:
    print(f"Olá, tudo bem, {aluno}?")
    if aluno == "Tcheba": # depois de perguntar se está tudo bem, Tcheba vai responder...
        print("Coraçãozinho não tá batendo legal")
    else: # depois de perguntar se está tudo bem, cada um vai responder...
        print("Vou bem na prova")

# Funções
def tudo_bem(nome): # define uma função que precisa de um argumento 'nome'
    print(f"Tudo bem, {nome}?") # ao chamar a função, vai dar print nesta linha com o nome que você colocou como argumento
    return nome
# lembre-se que se você definir uma variável dentro de uma função, ela não vai aparecer no Variable Explorer!
# isso acontece pq ela é criada dentro do espaço da função e não existe no espaço global do script!
# os comandos de uma função precisam estar indentados!!!
tudo_bem("Luca") # chama a função para que ela seja executada