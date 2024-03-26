from module1 import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failise("päevad.txt")

paevad=loe_failist("Päevad.txt")

print(paevad)
for paev in paevad:
    print(paev)
