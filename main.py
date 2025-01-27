
raio = input("Entre com o raio do circulo: ") # input informado pelo usuário
# ps: a função input recebe apenas elementos Stings, com os quais não conseguimos fazer contas

raio = float(raio) # altera o tipo do 'raio' de String para float
#tambem pode ser usado: raio = float(input("Entre com o raio do circulo: "))

pi = 3.1415 # valor fixo

diametro = 2 * raio # 2 vezes raio
perimetro = 2 * pi * raio # 2 vezes pi vezes raio
area = pi * (raio ** 2) # pi * (raio elevado a 2)


print("Diametro:", diametro)

# preenche a variavel texto com todos os dados e depois só precisamos printa-la
texto = "Perimetro: %0.2f" %(perimetro) 
print(texto) 

print("Area: %0.2f" %(area))
# ps: %0.2f é usado dentro do print para definir que a variavel f (float) será apresentada com 2 casas decimais

