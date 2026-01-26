"""
Jogo Pedra, Papel e Tesoura em Python
Autor: Ricardo de Souza Jr

Descrição:
Jogo em terminal onde o usuário enfrenta a máquina no clássico
Pedra, Papel e Tesoura. O primeiro a fazer 3 pontos vence.
"""

import random


def verifica_vencedor(pontos_usuario, pontos_maquina):
    """Retorna True se alguém já atingiu 3 pontos."""
    return pontos_usuario >= 3 or pontos_maquina >= 3

def placar(pontos_usuario, pontos_maquina):
    print("\n============================")
    print("        PLACAR ATUAL        ")
    print("============================")
    print(f"Você    : {pontos_usuario}")
    print(f"Máquina : {pontos_maquina}")
    print("============================\n")

def placar_final(pontos_usuario, pontos_maquina):
    """Exibe o resultado final do jogo."""
    if pontos_usuario == pontos_maquina:
        return
    elif pontos_usuario > pontos_maquina:
        print(f"\nParabéns! Você venceu a Máquina por {pontos_usuario} X {pontos_maquina}!!")
    else:
        print(f"\nNão foi dessa vez… A Máquina venceu você por {pontos_maquina} X {pontos_usuario}")

def jogar():
    pontos_usuario = 0
    pontos_maquina = 0

    print("Que comecem os jogos!!")
    print("Desafie a Máquina em uma eletrizante batalha de PEDRA, PAPEL ou TESOURA!!")
    print("O primeiro com 3 pontos leva.\n")

    alternativas = ["r", "p", "t"]
    nome = {"r": "Pedra", "p": "Papel", "t": "Tesoura"}

    while True:
        if verifica_vencedor(pontos_usuario, pontos_maquina):
            break

        escolha_usuario = input(
            "\nR - Pedra\nP - Papel\nT - Tesoura\nQ - Encerrar jogatina\n\nESCOLHA: "
        ).lower()

        if escolha_usuario == "q":
            print("\nJogo encerrado pelo jogador.")
            break

        if escolha_usuario not in alternativas:
            print("Escolha inválida! Use apenas R, P, T ou Q.")
            continue

        alternativa_maquina = random.choice(alternativas)

        print("\nSua escolha || Escolha da Máquina")
        print(f"    {nome[escolha_usuario]}  X  {nome[alternativa_maquina]}")
        
        if alternativa_maquina == escolha_usuario:
            print("Empate!!")
            

        elif (alternativa_maquina == "r" and escolha_usuario == "t") or \
             (alternativa_maquina == "p" and escolha_usuario == "r") or \
             (alternativa_maquina == "t" and escolha_usuario == "p"):
            print("Você perdeu!! Vitória da Máquina.")
            pontos_maquina += 1

        else:
            print("Você ganhou!!!")
            pontos_usuario += 1

        placar(pontos_usuario, pontos_maquina)


    placar_final(pontos_usuario, pontos_maquina)


if __name__ == "__main__":
    jogar()

