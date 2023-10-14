

height = float(input("Say your height"))
weight = int(input("Say you weight"))

weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(bmi_as_int)

#two_digit_number = input(): Solicita ao usuário que insira um número de dois dígitos. O número é lido como uma string a partir do console e armazenado na variável two_digit_number.

#first_digit = int(two_digit_number[0]): Obtém o primeiro dígito do número lido (o dígito das dezenas) convertendo o primeiro caractere da string two_digit_number em um número inteiro. Essa informação é armazenada na variável first_digit.

#second_digit = int(two_digit_number[1]): Obtém o segundo dígito do número lido (o dígito das unidades) convertendo o segundo caractere da string two_digit_number em um número inteiro. Essa informação é armazenada na variável second_digit.

#two_digit_number = first_digit + second_digit: Realiza a soma dos dois dígitos (o dígito das dezenas e o dígito das unidades) e atribui o resultado à variável two_digit_number. Essencialmente, isso calcula o valor numérico total do número de dois dígitos.

#print(two_digit_number): Imprime o valor calculado, que é a soma dos dígitos do número de dois dígitos, no console.