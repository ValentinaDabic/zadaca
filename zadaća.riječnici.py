import random

studenti = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni', 'Tonka',
            'Antonio', 'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina', 'Karlo', 'David',
            'Ivan', 'Petar', 'Marija', 'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio', 'Renato', 'Matej', 'Matej',
            'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 'Petar', 'Dražen', 'Zvonimir', 'Marin', 'Antonio', 'Stipe', 'Ana',
            'Mate', 'Mizoslav', 'Karlo', 'Marino', 'Mija', 'Kristijan', 'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano',
            'Mate', 'Mateo', 'Harun']

ocjene = {}

for student in studenti:
    ocjena = random.randint(1, 5)
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1

broj_prolaznih = 0
ukupno_studenata = len(studenti)

for ocjena in range(2, 6):
    if ocjena in ocjene:
        broj_prolaznih += ocjene[ocjena]

postotak_prolaznosti = (broj_prolaznih / ukupno_studenata) * 100

print("Broj ocjena:")
print(ocjene)

print("Postotak prolaznosti: {:.2f}".format(postotak_prolaznosti))
