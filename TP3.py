"""
2025-10-27
Ivan Zheryakov
Combat de monstres
"""

import random

hp = 20
dice = random.randint(1, 6)
opposing_power = random.randint(1, 5)
play_game = True
options = ["combattre", "eviter et ouvrir une autre portes", "regles du jeu"]

while play_game:
    input("Appuyer pour commencer")
