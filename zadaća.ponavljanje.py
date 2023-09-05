import random

imena = ['Richard', 'Kevin', 'Edward', 'Debbie', 'Adam', 'Norma', 'Christopher', 'Karen', 'Tami', 'Michael', 'John',
         'Roseanna', 'Gerald', 'George', 'Vesta', 'Julie', 'Raymond', 'Janice', 'Susan', 'Kerry', 'Lorenzo', 'Holly',
         'Sherri', 'William', 'Karey', 'Marion', 'Melissa', 'Vincent', 'Ruby']

prezimena = ['Arnold', 'Simmons', 'Velasco', 'Canada', 'Gibbs', 'Thompson', 'Rendall', 'Harris', 'Hendon', 'Lyles',
             'Perez', 'Cleary', 'Hoyman', 'Hall', 'Baker', 'Fichter', 'Colantuono', 'Moose', 'Howard', 'Davis', 'Nutt',
             'Cornett', 'Smith', 'Lemus', 'Beltran', 'Ho', 'Cook', 'Samuels', 'Rodriguez', 'Cano']

radnici = []

# Generiranje radnika
for _ in range(15):
    ime = random.choice(imena)
    prezime = random.choice(prezimena)
    satnica = round(random.uniform(4, 6), 2)
    radnik = {"ime": ime, "prezime": prezime, "satnica": satnica}
    radnici.append(radnik)

#Dodavanje svojstava "tjedni_sati"
for radnik in radnici:
    radnik("tjedni_sati") = random.randint(20, 30)

isplate = []
ukupna_isplata = 0

for radnik in radnici:
    ime = radnik["ime"]
    prezime = radnik["prezime"]
    satnica = radnik["satnica"]
    tjedni_sati = radnik["tjedni sati"]
    isplata = round(satnica * tjedni_sati, 2)
    ukupna_isplata += isplata
    isplate.append((ime, prezime, isplata))

prosjecna_isplata = round(ukupna_isplata / len(radnici), 2)

for ime, prezime, isplata in isplate:
    print(f"ime: {ime}\nPrezime: {prezime}\nIsplata: {isplata}\n")

print(f"Ukupna isplata: {ukupna_isplata}")
print(f"Prosjecna isplata: {prosjecna_isplata}")

# Ispis imena radnika s isplatom iznad prosjeka
print("\nRadnici s isplatom iznad prosjeka:")
for ime, prezime, isplata in isplate:
    if isplata > prosjecna_isplata:
        print(f"{ime} {prezime}")
