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
showed_rules = False
opposing_power = 0
power = 0

input("Appuyer pour commencer")

while play_game:

    if hp <= 0:
        print(f"Vous êtes déchu(e) après {combat} combats.\n"
              f"Vous avez {combat_win} victoires et {combat_loss} defaites.")
        play_game = False
        continue
    if combat_win != 0:
        if combat_win % 3 == 0:
            opposing_power = random.randint(3, 5)
            print("Boss Time")
    else:
        if not showed_rules:
            opposing_power = random.randint(1, 5)
            power = 20#random.randint(1, 6)
        else:
            showed_rules = False

    print(f"Vous tombez face à face avec un adversaire de difficulté : {opposing_power}")
    options = int(input("1- combattre\n2- eviter et ouvrir une autre porte\n3- regle du jeu\n4- Quitter le jeu\n"))

    if options == 1:
        combat += 1

        if opposing_power < power:
            print(f"roulé(e) un {power}")
            combat_win += 1
            hp += opposing_power
            print(f"Bravo! Vous avez gagner grace à {power - opposing_power} pts de pouvoir de plus que l'ennemi!")
        else:
            combat_loss += 1
            print(f"roulé(e) un {power}")
            hp -= opposing_power
            print("Vous avez perdu... Meilleure chance la prochaine fois!")

        print(f"Force de l’adversaire: {opposing_power}\n"
              f"Niveau de vie de l’usager: {hp}\n"
              f"Combat:  {combat} \n"
              f"Victoires: {combat_win} vs. Defaites: {combat_loss}\n")

    elif options == 2:
        hp -= 1
        print(f"Niveau de vie de l’usager: {hp}")

    elif options == 3:
        showed_rules = True
        print("Vous êtes dans un donjon et vous lancez des dés pour survivre.\n"
              "- Si votre lancer de dé est supérieur à celui de votre ennemi,\n"
              "vous gagnez et passez au donjon suivant.\n"
              "- S'il est inférieur, vous perdez une vie.\n"
              "- Vous pouvez également choisir une autre porte en échange d'un point de vie.\n"
              "- Finalement, vous pouvez toujours quitter le jeu quand vous voulez.")
        input("Fermer")


    elif options == 4:
        print("Votre progrès ne sauvegarde pas! Bon soir.")
        play_game = False
