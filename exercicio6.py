def exercicioSeis(salario, percentualReajuste):
    if salario <= 0:
        return 'Informe um número positivo!'
    else:
        percentualReajuste = salario + (salario * percentualReajuste / 100)
        return percentualReajuste