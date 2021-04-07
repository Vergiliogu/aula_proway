# Criando uma função
"""
def nome_funcao():
    comandos...
"""
def teste():
    return "Oi"


# Chamando uam função
def teste():
    return "Oi"

teste() # Retorna "Oi"


# Definindo parâmetros para a função
def teste(nome, idade):
    return "Seu nome é " + nome + " e sua idade é " + str(idade)

teste("Gustavo", 100) # Retorna "Seu nome é Gustavo e sua idade é 100"


# Definindo argumentos com valor padrão
def teste(nome, idade=None):
    if idade:
        frase = nome + ", você tem " + str(idade) + " anos"
    else:
        frase = "Olá " + nome
    return frase

teste("Gustavo") # Retorna "Olá Gustavo"
teste("Gustavo", 100) # Retorna "Gustavo, você tem 100 anos"
