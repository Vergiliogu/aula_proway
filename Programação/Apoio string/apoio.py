# T e s t e
# 0 1 2 3 4

#  T  e  s  t  e
# -5 -4 -3 -2 -1

string = "Banana"

string
# e 
"Banana"
# são exatamente a mesma coisa


# Acessando um index só
"Teste"[1] # retorna "e"
"Teste"[-2] # retorn "t"


# Acessando por vário indexes
"Teste"[0:3] # retorna "Tes"
"Teste"[0:] # retorna "Teste"
"Teste"[:4] # retorna "Test" 
"Teste"[:] # retorna "Teste"
"Teste"[-5:-2] # retorna "Tes"

# Usando o passo
"Teste"[::2] # retorna "Tse"
"Teste"[1:4:2] # retorna "et"
"Teste"[::-1] # retorna "etseT"


# index() retorna o index de uma string dentro de outra
"Eu tenho uma banana".index("bana") # retorna 13
"Bananas são amarelas".index("Bananas") # retorna 0
# "Bananas são amarelas".index("bananas") # retorna um erro porque a string não está dentro da outra


# in retorna se uma string está dentro de outra
"ana" in "Banana" # retorna True
"la" in "Banana" # retorna False


# Juntando strings
"Banana" + "e uma" + "maçã" # retorna "Banana e uma maçã"


# Multiplicando strings
"Banana" * 5 # retorna "BananaBananaBananaBananaBanana"
"Banana" + "Oi" * 2 # retorna "BananaOiOi"
("Banana" + "Oi") * 2 # retorna "BananaOiBananaOi"





