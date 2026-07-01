hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    =========
    """, 
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    =========
    """, 
    """
     +---+
     |   |
     O   |
    /|   |
         |
    =========
    """, 
    """
     +---+
     |   |
     O   |
     |   |
         |
    =========
    """, 
    """
     +---+
     |   |
     O   |
         |
         |
    =========
    """, 
    """
     +---+
     |   |
         |
         |
         |
    =========
    """  
]
import random
mot = ["esquiver", "surgir", "dissimuler", "entamer", "prolonger", "déceler", "entrecroiser",
"persister", "susciter", "entraver"]
import_choise = random.choice(mot)

display = list("_" * len(import_choise))
print(hangman_stages[6])
print(" ".join(display))

essais = 6
lettres_devinees = []
while "_" in display and essais > 0:
    guessed = input("Devinez une lettre: ").lower()
    if guessed in lettres_devinees:
        print(f"Vous avez déjà deviné la lettre '{guessed}' ! Vos essais restent {essais}.")
        print(hangman_stages[essais])
        print(" ".join(display))
        continue
    lettres_devinees.append(guessed)

    if guessed not in import_choise:
        essais -= 1
        print(f"Choisissez Fausse ! Il vous reste {essais} essais.")
    else:
        print(f"Choisissez correct ! Il vous reste {essais} essais.")

    
    for position in range(len(import_choise)):
        leterr = import_choise[position]
        if leterr == guessed:
            display[position] = guessed
    print(hangman_stages[essais])
    print(" ".join(display))

if "_" not in display:
    print("""          **********
          tu gagnes
          **********""")
else:
    print(f"Tu as perdu! Le mot était: {import_choise}")
    print("""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |""")
