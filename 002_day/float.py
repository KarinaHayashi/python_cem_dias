#"100.05" é uma string que representa um número decimal.
#float("100.05") converte essa string em um número de ponto flutuante (float), ou seja, um número com casas decimais. Portanto, float("100.05") resultará em 100.05 como um valor numérico de ponto flutuante.
#70 é um número inteiro.
#70 + float("100.05") realiza uma adição entre o número inteiro 70 e o número de ponto flutuante 100.05.
#O resultado da adição é 170.05.
#print(70 + float("100.05")) imprime o valor resultante, 170.05, no console.
#Portanto, o código soma 70 ao valor convertido da string "100.05" e imprime o resultado, que é 170.05. A conversão da string para um número de ponto flutuante é necessária para realizar a operação matemática corretamente.

print(70 + float("100.05"))

#---------------

#70 é um número inteiro.
#str(100) converte o número inteiro 100 em uma string, porque você está tentando concatená-lo com um número.
#Quando você tenta somar 70 com a string "100", ocorre um erro de tipo, porque você não pode somar um número com uma string diretamente em Python.
#Para corrigir o erro, você pode converter o número inteiro em uma string e, em seguida, concatená-lo. Aqui está uma versão corrigida:
#print(str(70) + str(100))
#Isso irá converter ambos os números em strings e, em seguida, concatená-los, resultando em "70100" como saída.

print(str(70) + str(100))

print (3 * 3 / 3 + 3 - 3)

print (3 * (3+3) / 3 -3)