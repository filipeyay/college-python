import random

def get_escolha():
    j_escolha = input("Escolha um (pedra/papel/tesoura): ") # escolha do jogador
    opcoes = ["pedra", "papel", "tesoura"]
    c_escolha = random.choice(opcoes) # escolha da maquina
    escolha = { "jogador": j_escolha, "computador": c_escolha }
    return escolha

def check_vitoria(jogador, computador):
    print(f"O jogador escolheu {jogador}, a maquina escolheu {computador}.")
    if jogador == computador:
        return "Empate!"
    elif jogador == "pedra":
        if computador == "tesoura":
            return "Pedra esmaga tesoura! Vitoria!"
        else:
            return "Papel cobre pedra! Você perdeu."
    elif jogador == "papel":
        if computador == "rock":
            return "Papel cobre pedra! Vitoria!"
        else:
            return "Tesoura corta papel! Você perdeu."
    elif jogador == "tesoura":
        if computador == "papel":
            return "Tesoura corta papel! Vitoria!"
        else:
            return "Pedra esmaga tesoura! Você perdeu."
        
escolha = get_escolha()
resultados = check_vitoria(escolha["jogador"], escolha["computador"])
print(resultados)