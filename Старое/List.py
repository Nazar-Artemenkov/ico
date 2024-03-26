import random

valikud = ["kivi", "käärid", "paber"]
raundide_arv = int(input("Mitu raundi soovite mängida? "))
kasutaja_punktid = 0
arvuti_punktid = 0
for raund in range(1, raundide_arv + 1):
    print(f"\nRaund {raund}/{raundide_arv}")
    kasutaja_valik = input("Valige kivi, käärid või paber: ").lower()
    if kasutaja_valik not in valikud:
        print("Vigane sisend. Palun proovige uuesti.")
        continue
    arvuti_valik = random.choice(valikud)
    print(f"Te valisite {kasutaja_valik}. Arvuti valis {arvuti_valik}.")
    if kasutaja_valik == arvuti_valik:
        print("Viik!")
    elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik == "käärid" and arvuti_valik == "paber") or \
         (kasutaja_valik == "paber" and arvuti_valik == "kivi"):
        print("Te võitsite!")
        kasutaja_punktid += 1
    else:
        print("Te kaotasite!")
        arvuti_punktid += 1
print("\nMäng lõppenud!")
print(f"Teie punktid: {kasutaja_punktid}")
print(f"Arvuti punktid: {arvuti_punktid}")
if kasutaja_punktid > arvuti_punktid:
    print("Te võitsite mängu!")
elif kasutaja_punktid < arvuti_punktid:
    print("Te kaotasite mängu!")
else:
    print("Mäng lõppes viigiga!")








#from random import *
#list_= []
#m=randint(1,
#for i in range(m):
#     list_.insert(i,randint(1,1000))
#max_=max(list_)
#arv=max_/m
#indeks=list_.index(max_)
#list_[indeks]=arv


#print(list_)







##from random import *
##from string import *
#Indeksid=["Tallinn","Narva","Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa,Jõgevamaa","Tartu linn", "Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","äänemaa, Hiiumaa, Saaremaa"]
#while True:
#    indeks=input("Indeks:")
#    if len(indeks)==5  and indeks.isdigit():
#        break
#    else:
#        print("Ainult 5 numbriline arv saab kontrollida!")

#print(indeks, "Kasustatakse", Indeksid[int(indeks[0])-1])
#maakond=(Indeksid[int(indeks[0])-1])
#if maakond in ("Tallinn","Narva","Kohtla-Järve"):
#    print("Оставайтесь дома!")
#else:
#    print("Носите маски!")



##3
#while True: 
#    sym=input("Mis sübol kasutame?")
#    if sym in punctuation: 




#        break 
#    else:
#        print("Saab kasutada ainult: !#$%&'()*+,-./:;<=>?@[\]^_`{|}~.")
#while True:
#    try:
#       N=int(input("Raidade arv: "))
#       break
#    except TypeError:
#        print("Ainult täisarvud")
#for i in range(N):
#    print(randint(1,50)*sym)


    

#nimed = ["Mati", "kati"]

#while True:
#    try:
#        valik = input("andmete lisamine - add\nAndmete näitamine - show\n")
        
#        if valik == "add":
#            valik = input("Kas lisame mitu inimest või positsioonile (pos)\nAndmete kustutamine - del\nJärjendi pööramine - rev\nAndmete kustutamine - clear\nAndmete sortimine - sort\nAndmete otsing - ots\n")
            
#            if valik == "mitu":
#                mitu = int(input("Mitu inimest lisame? "))
#                for i in range(mitu):
#                    nimi = input("Sisesta nimi: ")
#                    nimed.append(nimi)
#            else:
#                indeks = int(input("Kuhu lisamine?"))
#                nimi = input("Mis nimi: ")
#                nimed.insert(indeks-1, nimi)
        
#        elif valik == "del":
#            valik = input("Kas kustutame nimi (nimi) või indeksi järgi (ind)?")
#            if valik == "nimi":
#                nimi = input("Mis nimi on vaja kustutada?")
#                kogus = nimed.count(nimi)
#                if kogus > 0:
#                    for i in range(kogus):
#                        nimed.remove(nimi)
#                else:
#                    print(f"Nimi {nimi} ei ole nimekirjas")
#            else:
#                indeks = int(input("mis on järjekorranumber?"))
#                nimed.pop(indeks-1)
        
#        elif valik == "show":
#            print(nimed)
        
#        elif valik == "rev":
#            nimed.reverse()
#            print(nimed)
        
#        elif valik == "sort":
#            nimed.sort()
#            print(nimed)
        
#        elif valik == "clear":
#            nimed.clear()
#            print("Nimekiri on tühi")
        
#        elif valik == "ots":
#            ind = -1
#            nimi = input("Mis nime otsime?") 
#            if nimed.count(nimi) > 0:
#                for nim in nimed:
#                    if nim == nimi:
#                        ind = nimed.index(nimi, ind+1)
#                        print(f"{nimi} on indeksiga {ind}")
#            else:
#                print(f"{nimi} ei ole nimekirjas")

#    except ValueError as ve:
#        print(f"Error: {ve}. Please enter a valid number.")
#    except Exception as e:
#        print(f"An unexpected error occurred: {e}")
