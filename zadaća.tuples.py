
ime = ['Mario', 'Josip', 'Ivana', 'Mija', 'Ivan', 'Ante', 'Marino', 'Ana-Marija', 'Frano', 'Mladen', 'Marko', 'Jozo Matej',
       'Karlo', 'Mate', 'Katarina', 'Tomislava', 'Alija', 'Sara', 'Petar', 'Safet', 'Matej', 'Stjepan', 'Ivan', 'Antonio',
       'David', 'Ivan Entoni', 'Marija', 'Mate', 'Kristijan', 'Antonio', 'Ružica', 'Petar', 'Ana', 'Zvonimir', 'Matea',
       'Petar', 'Miroslav', 'Matea', 'Marija', 'Marko', 'Antonio', 'Matej', 'Iva', 'Leonardo', 'Karlo', 'Josip', 'Ivan',
       'Vice', 'Azer']

prezime = ('Jonjić', 'Cavar', 'Bunoza', 'Sabljić', 'Luetić', 'Šimić', 'Rupar', 'Bakula', 'Vranjković', 'Tomić', 'Benković',
           'Lasić', 'Rezo', 'Penava', 'Galić', 'Bopa', 'Kičin', 'Budimir', 'Lončar', 'Szna', 'Knežević', 'Marić', 'Udovičić',
           'Jakovljević', 'Grubišić', 'Bunoza', 'Krištić', 'Zeljko', 'Sliškovio', 'Bebek', 'Grgić', 'Ilišević', 'Šimić',
           'Milardović', 'Tufekčić', 'Markić', 'Pinjuh', 'Bošnjak', 'Krištić', 'Cubela', 'Mlikota', 'Kraljević', 'Šimovič',
           'Karačić', 'Bagarić', 'Jurković', 'Živković', 'Božić', 'Džemić')

bodovi = ('100', '100', '100', '90', '80', '75', '60', '60', '55', '55', '55',
          '50', '50', '50', '50', '50', '50', '40', '35', '35', '30', '30', '25',
          '25', '20', '20', '20', '15', '15', '15', '15', '15', '10', '150', 
          '10', '10', '5', '5', '5', '5', '0', '0', '0', '0', '0', '0', '0', '0', '0')
ocjene = ('5', '5', '5', 'S', '4', '3', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2' , 'Nije položio/la',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio', 'Nije položio', 'Nije položio',
          'Nije položio', 'Nije položio')


ucenici = list(zip(ime, prezime, bodovi))
polozili = [ucenik for ucenik in ucenici if int(ucenik[2]) >= 49]
for ime, prezime, bod in polozili :
    print(ime, prezime)
    
ucenici_sortirani = sorted(ucenici, key=lambda x: x[1])  #Sortiranje po prezimenima

rjecnik_ocjena = {}  #Novi riječnik za bodovne rangove

for bod, ocjena in zip(bodovi, ocjene):
    bod = int(bod)
    if bod <= 49:
        rjecnik_ocjena.setdefault('Nedovoljan', 0)
        rjecnik_ocjena['Nedovoljan'] += 1
    elif 50 <= bod < 65:
        rjecnik_ocjena.setdefault('Dovoljan', 0)
        rjecnik_ocjena['Dovoljan'] += 1
    elif 66 <= bod <= 80:
        rjecnik_ocjena.setdefault('Dobar', 0)
        rjecnik_ocjena['Dobar'] += 1
    elif 81 <= bod <= 90:
        rjecnik_ocjena.setdefault('Vrlodobar', 0)
        rjecnik_ocjena['Vrlodobar'] += 1
    elif 91 <= bod <= 100:
        rjecnik_ocjena.setdefault('Izvrstan', 0)
        rjecnik_ocjena['Izvrstan'] += 1

print("Sortirani učenici po prezimenima:")
for ime, prezime, bod in ucenici_sortirani:
    print(prezime, ime)

print("\nRiječnik ocjena po bodovnom rangu:")
for rang, broj_ocjena in riječnik_ocjena.items():
    print(f"{rang}: {broj_ocjena}")
