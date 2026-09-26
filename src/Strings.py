"""
STRINGS (SIGNA)
    Neste arquivo veremos o que é uma string. 
    
    Você pode até estar pensando que nunca viu isso ou que não conhece esse 
    nome, mas provavelmente já teve contato com uma string. Ela está apenas 
    com uma nomenclatura diferente. 
    
    Este próprio texto que você está lendo é uma string. Porém, neste caso, 
    ele é chamado de docstring, pois é uma string utilizada para documentar 
    um módulo, função, classe ou método. 
    
    Você também viu strings dentro da função print() nos arquivos anteriores. 
    Provavelmente já deve ter tido uma ideia do que é uma string. 
    
    Uma string é uma sequência de caracteres que o Python identifica como um 
    objeto do tipo texto. 
    
    No Python, o tipo utilizado para representar strings é chamado de str. 
    
    Exemplos: 
        "Hello World!" 
        'Python' "123" 
        'Olá, mundo!' 
    
    Mesmo "123" sendo composto apenas por números, quando escrito entre aspas 
    ele é tratado pelo Python como uma string (str), e não como um número (int).
"""

# Ex. 1: 
# Uma variável pode ser associada a um objeto do tipo str. 
nome = "Dragon" 
print(nome) 

# Ex. 2:
# Strings podem ser delimitadas utilizando aspas duplas ou aspas simples. 
nome_a = "Jhon" # String delimitada por aspas duplas. 
nome_b = 'Riquelmy' # String delimitada por aspas simples. 
print(nome_a) 
print(nome_b) 

# Ex. 3:
# Uma string não precisa possuir caracteres.
# Uma string vazia também é um objeto do tipo str.
texto = "" 
print(texto) 
print(len(texto))

# Ex. 4:
# Também podemos criar strings que ocupam múltiplas linhas. 
texto = """Texto: 
Em múltiplas linhas do código. 
Tchau!!""" 
print(texto)

# Ex. 5:
# Sequências de escape são utilizadas para representar caracteres
# especiais dentro de uma string.
texto = "Quebra\nde linha." # \n representa uma quebra de linha.
print(texto) 

texto_0 = "Uma sequência de escape\tque representa um tab." # \t representa uma tabulação.
print(texto_0)

texto_1 = "C:\\User\\Jhon" # \\ representa uma barra invertida (\) dentro da string.
print(texto_1)

texto_2 = "Ela disse 'oi'" 
# Podemos utilizar aspas simples dentro de uma string delimitada
# por aspas duplas.
print(texto_2) 

texto_3 = "Ela disse \"oi\"" 
# Também podemos utilizar uma sequência de escape para representar
# # aspas duplas dentro de uma string delimitada por aspas duplas.
print(texto_3)

# Ex. 6:
# Concatenação de strings.
# A concatenação consiste em unir duas ou mais strings,
# formando uma nova string.
frase = "Olá, " + nome
print(frase) 

# Ex. 7:
# Repetição de uma string.
# O operador * pode ser utilizado para criar várias repetições
# de uma mesma string.
texto = "Python " * 5 
print(texto) 

# Ex. 8:
# Índices e fatiamento de strings.
# Cada caractere de uma string possui uma posição, chamada de índice.
# A contagem dos índices começa em 0. 
texto = nome_a[0] 
print(texto) # O fatiamento permite obter uma parte da string.

# Neste exemplo, serão obtidos os caracteres dos índices 0 e 1.
letras = nome_a[0:2]
print(letras) 

# Ex. 9:
# A função len() retorna a quantidade de elementos de um objeto.
# len() é uma função nativa do Python.

# No caso de uma string, ela retorna a quantidade de caracteres.
quantidade = len(letras)
print(quantidade) 

# Ex. 10:
# Os operadores in e not in verificam se determinado valor está
# presente ou não em uma sequência.
print("J" in nome_a) # Verifica se o caractere "J" está presente em nome_a.
print("J" not in nome_b) # Verifica se o caractere "J" não está presente em nome_b.

# Ex. 11:
# Métodos comuns utilizados para manipulação de strings.
print(frase.upper()) # upper() retorna uma nova string com os caracteres em maiúsculas.
print(frase.lower()) # lower() retorna uma nova string com os caracteres em minúsculas.

texto = " Oi com muito espaço no final " 
print(texto.strip()) # strip() remove espaços em branco do início e do final da string.

# Ex. 12:
# O método replace() substitui uma parte da string por outra.
nova_frase = frase.replace(nome, nome_a)
print(nova_frase)

# Ex. 13:
# Os métodos split() e join() podem ser utilizados em conjunto
# para dividir e unir strings. 
# split() divide uma string em uma lista utilizando um delimitador.
# join() une os elementos de uma sequência utilizando um delimitador.
nova_frase = frase.split(",")
print(nova_frase)

frase_original = ",".join(nova_frase)
print(frase_original)

# Ex. 14:
# Strings são imutáveis.
# Isso significa que métodos como upper(), lower() e replace()
# não modificam a string original.
# Eles retornam uma nova string.
texto = "Python"
texto.upper()
print(texto) # O resultado continua sendo "Python".

texto = texto.upper()
print(texto) # Agora a variável texto recebeu a nova string "PYTHON".

# Ex. 15:
# Formatação de strings.
# Existem diferentes formas de inserir valores dentro de uma string.
# Neste exemplo veremos três formas:
# 1. Formatação antiga com %
# 2. Método format()
# 3. F-string
altura = 1.78 
print("Meu nome é %s e minha altura é de %.2f metros" % (nome, altura)) # Forma antiga de formatação.

print("Meu nome é {} e minha altura é de {:.2f} metros".format(nome, altura)) 
# Formatação utilizando o método format().

print(f"Meu nome é {nome} e minha altura é de {altura:.2f} metros") # Formatação utilizando f-string.
# F-strings são uma forma moderna e prática de inserir valores
# de variáveis diretamente dentro de uma string.
# Particularmente, essa é a forma de formatação que eu mais gosto de usar.