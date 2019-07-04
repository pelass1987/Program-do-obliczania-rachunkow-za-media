cena_jed_gazu = 2.13
cena_jed_wody = 15.80
cena_jed_pradu = 0.54

prad_op_mc = 13.05 * 2
gaz_op_mc = 9.21 * 2
pln = "złotych"

gaz1 = int(input("Wpisz ilość jednostek gazu: "))
gaz = cena_jed_gazu * gaz1 + gaz_op_mc
print("Do zapłaty za gaz: ")
print(gaz)

woda1 = int(input("Wpisz ilość jednostek wody: "))
woda = cena_jed_wody * woda1
print("Do zapłaty za wodę: ")
print(woda)

prad1 = int(input("Wpisz ilość jednostek prądu: "))
prad = cena_jed_pradu * prad1 + gaz_op_mc
print("Do zapłaty za prąd: ")
print(prad)

print("W sumie do zapłaty za media: ")
print(float(gaz + woda + prad))
print(pln)




