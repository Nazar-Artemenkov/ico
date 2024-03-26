from module_registr import *


salasõnad=loe_failist("C:/Users/opilane/source/repos/register2-master/Регистрация/salasõnad1.txt")
kasutajanimed=loe_failist("C:/Users/opilane/source/repos/register2-master/Регистрация/Kasutajad.txt")
while True:
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutnime\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sisestage arv"))
    if vastus==1:
        print("registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed,salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime, parooli või mõlemad")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nimi muutmine: ")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine: ")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
    elif vastus==4:
        print("Unustanud paaaroli taastamine")
        kasutajanimed = parooli_vahetus_kasutajal(kasutajanimed)
        salasõnad = parooli_vahetus_kasutajal(salasõnad)
    elif vastus==5:
        print("Lõpetamine")
        break
    else:
        print("Tundmatu valik")
