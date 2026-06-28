import random
mot = ["esquiver", "surgir", "dissimuler", "entamer", "prolonger", "déceler", "entrecroiser", "persister", "susciter", "entraver"]
import_choise = random.choice(mot)
display = list("_" * len(import_choise))
print(" ".join(display))
essais = 6
while "_" in display and essais > 0:
    guessed = input("Devinez une lettre: ").lower()
    letter_found = False
    for position in range(len(import_choise)):
        leterr = import_choise[position]
        if leterr == guessed:
            display[position] = guessed
            letter_found = True
    if not letter_found:
        essais -= 1 
        print(f"Choisissez Fausse ! Il vous reste {essais} essais.")
    else:
        print(f"Choisissez correct ! Il vous reste {essais} essais.")
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
