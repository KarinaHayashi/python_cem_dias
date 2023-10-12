
#data types

#string

#com len nós podemos ver quantos caracteres tem em uma string
print(len("hello"))
#aqui podemos ver a posição da letra em Hello
#Se eu colocar o 0, vamos perceber que o H esta em primeiro, pois é o primeiro caractere dessa string
#É realmente importante lembrar que os programadores começam sempre a contar do zero, pois trabalhamos com binários, zeros e uns
print ("Hello"[0])

#se eu tentar imprimir "123" + 345" o que vai acontacer?

print("123" + "345")

#se você esperava uma soma e esta não ocorreu, deve ser pelo motivo de que "123" + "345" basicamente concatenou essa string

#integer

#então se quisermos somar dois números interios, sem nenhuma casa decimal, para isso temos que escrever o número sem nada (sem as aspas)

print(123 + 345)

#float
#então se quisermos somar dois números para obter um número decimal ou mesmo usar um número decimal na nossa programação, usamos o float

print(1.56 + 3.08)
print("3.14159")

#boolean
#em boolean nós temos apenas dois valores, que é o verdadeiro ou falso
bts_paved_the_way = True

if bts_paved_the_way:
    print("BTS PAVED THE WAY!")
else:
    print("BTS DID NOT PAVE THE WAY!")


street_name = "Abbey Road"
print(street_name[4] + street_name[7])