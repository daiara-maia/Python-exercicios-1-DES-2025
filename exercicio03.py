# Rafael trabalha com armazenamento de grãos e precisa garantir que a umidade do ar no local não ultrapasse 70%.
# Escreva um programa que receba o valor da umidade atual e exiba um alerta se estiver acima do limite.
unidade = int (input("digite a unidade."))
if unidade < 70:
   print("a temperatura esta boa.")
else:
   print("alerta temperatura utrapassou o limite.")
