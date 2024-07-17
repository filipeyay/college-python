import time
from calendar import isleap


def definir_ano_bissexto(ano):
    if isleap(ano):
        return True
    else:
        return False


def dias_mes(mes, ano_bissexto):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2 and ano_bissexto:
        return 29
    elif mes == 2 and (not ano_bissexto):
        return 28


nome = input("digite o seu nome: ")
idade = input("digite a sua idade: ")
horalocal = time.localtime(time.time())
ano = int(idade)
mes = ano * 12 + horalocal.tm_mon
dia = 0
inicio_ano = int(horalocal.tm_year) - ano
fim_ano = inicio_ano + ano

for y in range(inicio_ano, fim_ano):
    if definir_ano_bissexto(y):
        dia = dia + 366
    else:
        dia = dia + 365

ano_bissexto = definir_ano_bissexto(horalocal.tm_year)
for m in range(1, horalocal.tm_mon):
    dia = dia + dias_mes(m, ano_bissexto)

dia = dia + horalocal.tm_mday
print("A idade de %s é %d anos ou " % (nome, ano), end="")
print("%d meses ou %d dias" % (mes, dia))
