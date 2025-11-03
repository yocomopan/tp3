"""
2025-10-27
Ivan Zheryakov
Combat de monstres
"""

import random

hp = 20
combat = 0
combat_win = 0
combat_loss = 0
play_game = True
Game = True
"""
def options()
    
    
"""
input("Appuyer pour commencer")

while play_game:
    opposing_hp = random.randint(5, 20)
    opposing_power = random.randint(1, 6)
    print(f"Vous tombez face à face avec un adversaire de difficulté : {opposing_power}")

    options = int(input("1- combattre\n2- eviter et ouvrir une autre porte\n3- regle du jeu\n4- Quitter le jeu\n"))
    if options == 1:
        combat += 1
        battle_info = input(f"Vie d'adversaire: {opposing_hp}\nForce de l’adversaire: {opposing_power}\nNiveau de "
                            f"vie de l’usager: {hp}\nCombat {combat}: \nVictoires: {combat_win} vs. Defaites: {
                            combat_loss}\n")
        dice = random.randint(1, 6)
    elif options == 2:
        hp -= 1
        print(f"Niveau de vie de l’usager: {hp}")

    else:
        print("non")
        play_game = False
