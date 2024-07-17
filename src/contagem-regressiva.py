import time


def contagem(t):
    while t:
        minutos, segundos = divmod(t, 60)
        temporizador = "{:02d}:{:02d}".format(minutos, segundos)
        print(temporizador, end="\r")
        time.sleep(1)
        t -= 1

    print("O tempo acabou!")


t = input("Digite o tempo em segundos: ")

contagem(int(t))
