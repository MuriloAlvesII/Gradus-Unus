"""
VARIAVEIS (VARIABILES)

    Nesta parte, veremos o que são variáveis em Python e como utilizá-las em nossos programas. 
    
    Em Python, uma variável é criada quando associamos um nome a um objeto utilizando o 
    operador de atribuição "=". 
    
    Por exemplo: 
        nome = "Dragon" 
    
    Nesse caso, o nome "nome" passa a estar associado ao objeto "Dragon". 
    É importante observar que "=" não significa "igual". Ele é utilizado para realizar uma atribuição. 
    
    Também existem regras e convenções para a criação dos nomes utilizados nas variáveis.
"""

# Ex. 1: 
nome = "Dragon" # "nome" está associado ao objeto "Dragon".
idade = 2000 
cidade = "Pau dos Ferros"  

# Podemos utilizar o nome da variável para acessar o objeto associado a ele.
print("Ex.1:\n Ola!\n Meu nome é ", nome)
print(" Idade:", idade) 
print(" Cidade:", cidade)

# Ex. 2: 
# Podemos utilizar variáveis para realizar operações.
ano_atual = 2026
ano_nascimento = 26

idade = ano_atual - ano_nascimento

print("Ex.2:\n Eu nasci no ano ", ano_nascimento,".")
print(" Minha idade é", idade,".")

# Ex. 3:
# Uma variável pode ser associada a outro objeto posteriormente.
ano = 2026

print("Ex.3:\n Estamos no ano de", ano,".")

ano = 2030

print(" Estamos no ANO DE", ano,"!!!!????")
# Depois da nova atribuição, o nome "ano" passa a estar associado ao objeto 2030.

# Ex. 4:
# Podemos realizar múltiplas atribuições em uma única instrução.
nome, idade, cidade = "Frank", 15, "Água Nova"

print("Ex.4:\n Meu nome é", nome,"!")
print(" Moro na cidade de", cidade,".") 
print(" Tenho", idade, "anos de idade.")

# Ex. 5:
# Também podemos associar o mesmo objeto a vários nomes.
a = b = c = d = 0

print("Ex.5:\n a = ", a)
print(" b =", b)
print(" c =", c) 
print(" d =", d) # Nesse caso, os quatro nomes foram associados ao objeto 0.

# Nomes válidos:

nome = "Dragon"
idade_master = 2000
ano2026 = 2026
cidade_mora = "Pau dos Ferros"

# Nomes inválidos: 

# 2nome = "Dragon"
# Não pode começar com um número.

# idade-master = 2000 
# O hífen (-) é interpretado como operador de subtração.

# class = "Python"
# "class" é uma palavra reservada da linguagem Python.

""" 
REGRAS BÁSICAS PARA NOMES 
    1. Podem conter letras, números e underscore (_). 
    2. Não podem começar com um número. 
    3. Não podem conter espaços. 
    4. Não podem utilizar palavras reservadas do Python. 
    5. Python diferencia letras maiúsculas de minúsculas. 

        Exemplos: 
            nome = "Dragon" 
            nome_completo = "Dragon Saiyajin" 
            idade2 = 18 

        Convenção recomendada: 
            nome_completo 
            ano_nascimento 
            cidade_mora
"""