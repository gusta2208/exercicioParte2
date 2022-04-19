import exercicio1
import exercicio11
import exercicio12
import exercicio3
import exercicio2
import exercicio4
import exercicio5
import this

import exercicio6
import exercicio8

this.opcao = 0
num1 = 0

def mostrarMenu():
    print('Escolha uma das opções abaixo: '+
          '\n1 Exercicio 1' +
          '\n2 Exercicio 2' +
          '\n3 Exercicio 3' +
          '\n4 Exercicio 4' +
          '\n5 Exercicio 5' +
          '\n6 Exercicio 6' +
          '\n7 Exercicio 7' +
          '\n8 Exercicio 8' +
          '\n9 Exercicio 9' +
          '\n10 Exercicio 10' +
          '\n11 Exercicio11' +
          '\n12 Exercicio12' +
          '\n0 Sair')
    this.opcao = int(input())#coletar a digitação do usuario

def coletarNum1():
    print('Informe o primeiro número: ')
    this.num1 = float(input())
def coletarNum2():
    print('Informe o segundo número: ')
    this.num2 = float(input())
def coletarNum3():
    print('Informe o terceiro número: ')
    this.num3 = float(input())
#Exercicio 03
def coletarBase():
    print('Informe a base: ')
    this.base = float(input())
def coletarAltura():
    print('Informe a altura: ')
    this.area = float(input())
#Exercicio 11
def coletarSalarioFixo():
    print('Digite o salario fixo do vendedor: ')
    this.fixo = float(input())
def coletarVenda():
    print('Valor total de vendas: ')
    this.venda = float(input())
#Exercicio 12
def coletarNumConta():
    print('Informe o número da conta: ')
    this.conta = float(input())
def coletarDebito():
    print('Informe o valor do débito: ')
    this.debito = float(input())
def coletarCredito():
    print('Informe o valor do credito: ')
    this.credito = float(input())
#Exercicio 05
def coletarEleitores():
    print('Informe o total de eleitores: ')
    this.eleitores = float(input())
def coletarValidos():
    print('Informe os validos: ')
    this.validos = float(input())
def coletarNulos():
    print('Informe os nulos: ')
    this.nulos = float(input())
def coletarBrancos():
    print('Informe os votos Brancos')


#Exercicio 06
def coletarSalario():
    print('Informe o salário: ')
    this.salario = float(input())
def coletarPercentual():
    print('Informe o percentual de reajuste: ')
    this.percentual = float(input())


def operecao():
    #Mostrar o menu em tela
    while this.opcao != 10:
        mostrarMenu()
        if this.opcao == 1:
            print(exercicio1.exercicioUm(this.num1))
        elif this.opcao == 2:
            coletarNum1()
            print(exercicio2.exercicioDois(this.num1))
        elif this.opcao == 3:
            coletarBase()
            coletarAltura()
            print(exercicio3.areaRetangulo(this.base, this.area))
        elif this.opcao == 8:
            coletarNum1()
            coletarNum2()
            coletarNum3()
            print(exercicio8.exercicioOito(this.num1, this.num2, this.num3))
        elif this.opcao == 12:
            coletarNumConta()
            coletarDebito()
            coletarCredito()
            print(exercicio12.exercicioDoze(this.conta, this.debito, this.credito))
        elif this.opcao == 11:
            coletarSalarioFixo()
            coletarVenda()
            print(exercicio11.execicioOnze(this.fixo, this.venda))
        elif this.opcao == 6:
            coletarSalario()
            coletarPercentual()
            print(exercicio6.exercicioSeis(this.salario, this.percentual))
        elif this.opcao == 0:

            print('Obrigado!')
        else:
            print('Opção escolha inválida, tente novamente!')


