from minaOmaModule import *

kasutajad=["Nazar"]
paroolid=["Artemenkov"]
kus_vas=loe("Anket.txt")

while True:
    print("1-soorita test\n2-logi administraatorina sisse\n3-lõpetamine")
    vastus=int(input("Sisestage arv "))

    if vastus==1:
        print("Soorita test")
        osaleja_nimi=input("Palun sisestage oma nimi: ")
        N=int(input("Mitu küsimust soovid esitada? "))
        punktid=küsimus_vastus(kus_vas, N)
        salvesta(osaleja_nimi, punktid, "Oiged.txt", "Valed.txt")
        print("\nEdukalt läbinud osalejad:")
        oiged_fail=open("Oiged.txt",'r',encoding='utf-8')
        print(oiged_fail.read())
        oiged_fail.close()
        print("\nEbaõnnestunud osalejad:")
        valed_fail=open("Valed.txt",'r',encoding='utf-8')
        print(valed_fail.read())
        valed_fail.close()
    elif vastus==2:
        print("Administraator")
        autoriseerimine(kasutajad,paroolid)
        uued={}
        uute_arv=int(input("Mitu uut küsimust soovid lisada? "))
        for i in range(uute_arv):
            küsimus=input("Sisestage uus küsimus: ")
            vastus=input("Sisestage vastus uuele küsimusele: ")
            uued[küsimus]=vastus
        lisa(uued,"Anket.txt")
    elif vastus==3:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
