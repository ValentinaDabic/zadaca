import re

email = input("Unesite mail: ")
regex = "(^([a-zA-Z].*)[.]([a-zA-Z].*)@fpmoz.sum.ba$"
result = re.match(regex, email)

edu = input("Unesite eduId: ")
regexl = "^([a-zA-Zg)([a-zA-Z].*)[0-9]*@sum.ba$"
resultl = re.match(regexl, edu)

if result:
    print("Email tocan")
    if resultl:
     print("EduId tocan")
    else:
     print("EduId nije tocan")
else:
 print("Email nije tocan")
 if resultl:
   print("EduId tocan")
 else:
   print("EduId nije tocan")
        
    
              
