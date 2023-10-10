name = input("Whats your name?")
print("Hello " + (name))


print("Hello " + input("What is your name?"))

#input("What is your name?" é uma função de entrada e esa print("Hello " + input("What is your name?")) é uma declaração
#por tanto nos temos um aninhado dentro do outro e quando executamos o código, o que ocorre é que ele pergunta o meu nome

#Imprimir  o número de uma string de uma palavra
#a função "len" é capaz de informar quantos caracteres existem em uma determinda string
name = input("Whats is your name?")
print("Seu nome tem " + str(len(name)) + " letras")

