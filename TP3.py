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
opposing_power = 0
power = 0
play_game = True
showed_rules = False
boss_time = False
list = []


input("Appuyer pour commencer")

while play_game:

    if hp <= 0:
        print(f"Vous êtes déchu(e) après {combat} combats.\n"
              f"Vous avez {combat_win} victoires et {combat_loss} defaites.")
        play_game = False
        continue

    if combat_win > 0 and combat_win % 3 == 0 and list[-1] == "win":  # if win is * of 3 & higher than 0
        print("!BOSS TIME!")
        boss_time = True
        opposing_power = random.randint(4, 5)
    else:
        if not showed_rules:
            opposing_power = random.randint(1, 5)
            power = random.randint(1, 6)
        else:
            showed_rules = False

    if boss_time:  # if active
        print(f"Vous tombez face à face avec un boss de difficulté : {opposing_power}")
    else:
        print(f"Vous tombez face à face avec un adversaire de difficulté : {opposing_power}")

    options = int(input("1- combattre\n2- eviter et ouvrir une autre porte\n3- regle du jeu\n4- Quitter le jeu\n"))

    if options == 1:
        combat += 1

        if opposing_power < power:
            print(f"roulé(e) un {power}")
            combat_win += 1
            hp += opposing_power
            list.append("win")  # list adds WIN
            print(f"Bravo! Vous avez gagner {opposing_power} vies additionnelles!")

        else:
            combat_loss += 1
            print(f"roulé(e) un {power}")
            hp -= opposing_power
            list.append("loss")  # list adds LOSS
            print("Vous avez perdu... Meilleure chance la prochaine fois!")

        print("-+- STATUS -+-\n"
              f"> Force de l’adversaire: {opposing_power}\n"
              f"> Niveau de vie de l’usager: {hp}\n"
              f"> Combat:  {combat} \n"
              f"> Victoires: {combat_win} vs. Defaites: {combat_loss}\n")

        count = len(list)
        if count == 3:
            list.pop(0)



    elif options == 2:
        hp -= 1
        print(f"|Niveau de vie de l’usager: {hp}|")

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

    if boss_time:
        boss_time = False
