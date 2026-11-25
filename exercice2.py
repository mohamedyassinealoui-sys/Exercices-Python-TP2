notem = float(input("entrer votre note de mathematique :"))
notei = float(input("entrer votre note de informatique :"))
notep = float(input("entrer votre note de physique :"))
s = notem + notei + notep
m = s/3
if m>=10:
 print("valide")
else:
     print("non valide")