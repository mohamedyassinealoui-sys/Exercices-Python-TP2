#promiere horaire ;
h1=int(input("entrer heureu :"))
m1=int(input("entrer minute :"))
s1=int(input("entrer seconde :"))
#deuscieme horaire :
h2=int(input("entrer heureu :"))
m2=int(input("rntrer minute :"))
s2=int(input("entrer seconde :"))
h5=h1*3600+m1*60+s1
h6=h2*3600+m2*60+s2
if h6<h5:
    print("erreur")
else:
    f = h6-h5
print("le resultat en second est :", f)