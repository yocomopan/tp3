"""
2025-10-27
Ivan Zheryakov
Combat de monstres
"""

import random

hp = 20
dice = random.randint(1, 6)
opposing_power = random.randint(1, 6)
opposing_hp = random.randint(5, 20)
combat = 0
combat_win = 0
combat_loss = 0
play_game = True
Game = True

input("Appuyer pour commencer")

while play_game:
    print(f"Vous tombez face à face avec un adversaire de difficulté : {opposing_power}")

    options = int(input("1- combattre\n2- eviter et ouvrir une autre porte\n3- regle du jeu\n4- Quitter le jeu\n"))

    if options == 1:
        combat += 1
        battle_info = input(f"Adversaire: {opposing_hp}\nForce de l’adversaire: {opposing_power}\nNiveau de vie "
                            f"de l’usager: {hp}\nCombat {combat}: Victoires {combat_win} vs. Defaites\n{
                            combat_loss}")

    elif options == 2:
        hp -= 1
        print(f"Niveau de vie de l’usager: {hp}")
    else:
        print("non")
        play_game = False

