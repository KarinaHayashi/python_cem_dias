print("welcome to the rollercoaster!")

height = int (input("What is your height in cm?"))

if height > 120:
    print("You can ride the rollercoaster!!!!")
else:
    print("Sorry :( You have to grow taller before you can ride")

#if (se): A declaração if é usada para testar uma condição. Se a condição for avaliada como verdadeira (ou seja, a condição é atendida),
# o bloco de código dentro do if é executado.

#else (senão): A declaração else é usada em conjunto com if. Se a condição dentro do if for avaliada como falsa (ou seja, a condição não é atendida),
# o bloco de código dentro do else é executado.

print("If and else condition")

if_else = input("Do you understand how if and else work? ")

if if_else.lower() == "yes":
    print("Wow, you understand the if-else condition.")
else:
    print("Hmm, you need to study more.")
