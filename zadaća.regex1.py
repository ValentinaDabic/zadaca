import re

string = str(input("Unesite neki string: "))
string = string.lower()

regex = r"v.*[0-5]+.*\s.*d$"

result = re.findall(regex, string)

if result:
    print("Podudaranje")
else:
    print("Nema podudaranja")
