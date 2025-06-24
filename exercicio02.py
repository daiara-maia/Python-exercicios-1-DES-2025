 dia01 = int(input("digite o tempo nessesario para entregar atividade x"))
dia02 = int(input("digite o tempo nessesario para entregar atividade y"))
dia03 = int(input("digite o tempo nessesario para entregar atividade z"))

 if dia01 < 0 or dia02 < 0 or dia03 < 0:
    print("erro negativo .")
else:
    soma = dia01 + dia02 + dia03
    print("tempo total da atividade: {soma} dias")


