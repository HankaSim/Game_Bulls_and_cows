"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

Bulls and cows

author: Hana Šimečková
email: simeckova.hana8@gmail.com
discord: Hanka Š.
"""
# Importy
import random

# Pozdravení uživatele + úvodní text
linka = "-" * 50
linka2 = "-" * 55
print(
"Hi there!",
linka,
"""I have generated a random 4 digit number for you. 
Let's play a bulls and cows game!""",
linka,
sep = "\n"
)

# Generování tajného čísla
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tajne_cislo = list()

cislo_1 = random.choice(cisla)
tajne_cislo.append(cislo_1)

cisla.remove(cislo_1)
cisla.append(0)

mod = True
while mod:
    if len(tajne_cislo) < 4:
        cislo = random.choice(cisla)
        tajne_cislo.append(cislo)
        cisla.remove(cislo)

    else:
        mod = False

# print(tajne_cislo)

# Počítadlo
count = 0

# Smyčka hádání
mod2 = True
while mod2:

    # Hráč hádá číslo
    tip = input("Enter a number:")

    # Počítadlo
    count = count + 1

    if not tip.isnumeric():
        print("The number must be numeric.")
        print(linka)
        continue
    
    elif len(tip) != 4:
        print("The number does not contain 4 digits.")
        print(linka)
        continue


    # Převod vloženého stringu na list čísel
    list_tip = list(tip)
    tip_cislo = [int(x) for x in list_tip]

 
    # BULLS and COWS

    # Knihovny obou čísel
    tip_cislo_k = {"prvni": tip_cislo[0], "druhe": tip_cislo[1],\
    "treti": tip_cislo[2], "ctvrte": tip_cislo[3]}
    tajne_cislo_k = {"prvni": tajne_cislo[0], "druhe": tajne_cislo[1],\
    "treti": tajne_cislo[2], "ctvrte": tajne_cislo[3]}

    bulls = 0
    cows = 0

    # Upozornění na duplikát/ nulu na začátku (ale program vyhodnotí tip, protože to přinese\
    # užitečné informace)
    if not len(tip_cislo) == len(set(tip_cislo)):
        print("(The secret number contains unique digits.)")

    if tip_cislo[0] == 0:
        print("(The secret number does not start with zero.)")
    

    # Pokračování hádání
    if tajne_cislo != tip_cislo:

        for number in tajne_cislo_k:

            if tajne_cislo_k[number] == tip_cislo_k[number]:
                bulls = bulls + 1

            else:
                if tajne_cislo_k[number] in tip_cislo_k.values():
                    cows = cows + 1

        # Výstup
        if bulls != 1 and cows != 1:
            print(bulls, "bulls", "|", cows, "cows")
        elif bulls == 1 and cows != 1:
            print(bulls, "bull", "|", cows, "cows")
        elif bulls != 1 and cows == 1:
            print(bulls, "bulls","|", cows, "cow")
        else:
            print(bulls, "bull", "|", cows, "cow")
        print(linka)

    else:
        print(
        linka2,
        f"Correct, you've guessed the right number in {count} guesses!",
        linka2,
        sep = "\n"
        )
        mod2 = False