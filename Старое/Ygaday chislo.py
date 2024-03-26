#import random

#def Начать_игру():
#    print("Я загадал число от 1 до 100.")
#    число_к = random.randint(1, 100)
#    ввод_п = ""

#    while ввод_п != "конец":
#        ввод_п = input("Угадай число (или введите 'конец' чтобы закончить) ")

#        if ввод_п == "конец":
#            print(f"Игра завершена. Правильное число было {число_к}.")
#            break

#        число_п = int(ввод_п)

#        if число_п < число_к:
#            print("Число больше, попробуйте еще раз.")
#        elif число_п > число_к:
#            print("Число меньше, попробуйте еще раз.")
#        else:
#            print(f"Правильное число! Это было {число_к}. Игра окончена.")
#            break

#print()
#print()
#print()
#print()
#for i in range(1, 11):
#    ruut = i **2
#    kuup = i ** 2
#    print(f"{I:2} {ruut:2} [kuup:3]")

        #korrutamine=5
#for i in range(1,11):          #9
#    tulemus =(i)*5
#    print(f"{i}* 5 = {tulemus}")_

#paaris=0
#paaritu=0
#for i in range(1,101):
#    if i%2==0:
#        print(f"(i)-paaris")
#        paaris+=1
#    else:
#        print(f"(i)-paaritu")
#        paaritu+=1

#for i in range(5):
#    number=randit(0,09)
#    print(number,end"")
#print()

#kasted=0
#while True:
#    vastus =input("osta elevant ära! Kirjuta 'elevant'")
#    kasted +=1

#    if vastus.lower() =='elevant':
#        print(f"Õige! Ostid elevanti ära {kasted} katsega.")
#        break
#    else:
#        print("Vale vastus.Proovi uuesti.")

#number=randint(1,100)
#katsed=3
#while katsed>0:
#    külaline = int(input())
#    if külaline == number:
#        print()
#        break
#    else:
#        katsed-=1
#        print()
#        if katsed == 0:
#            print()
#            break
#veelkord input().lower


#eesnimi=input("Mis on sinu nimi?").capitalize()
#if eesnimi=="Juku":
#    try:
#        vanus=int(input("Kui vana sa oled?"))
#        print("Jukule ostame ", end="")
#        if 0<vanus<=6 :
#            print("tasuta pilet")
#        elif 6<vanus<=14 :
#            print("lastepilet")
#        elif 14<vanus<=65 :
#            print("täispilet")
#        elif 65<vanus<=100 :
#            print("soodupilet")
#        else:
#            print("Viga andmetega!")
#    except :
#        print("Int formaat on vaja kasutada")
   
#else:
#    print("Mine ise kinno!")


#2


#nimi1 = input("Введите первое имя:").capitalize
#nimi2 = input("Введите второе имя:").capitalize
#if nimi1== "Oleg" and nimi2== "Nazar":
#        print(f" {nimi1} и {nimi2} сегодня ближайшие соседи!")
#else:
#        print("Введите имена обоих людей")

 #
 


 
#try:
#     pikkus = float(input("Введите длину комнаты:"))
#     try:
#         laius = float("Введите ширину комнаты: ")
#         S = pikkus * laius
#         print("Pindala võrdub", S)
#         soov=input("Kas tahad remondi teha?").lower()
#         if soov=="jah":
#             try:
#               hind=float(input("Ruutmeetri hind: "))
#               summa=hind*S
#               print("Remondi summa on", summa)
#             except :
#                 print("viga")
#             hind=float(input("Ruutmeetri hind: "))
#             summa=hind*S
#             print("Remondi summa on", summa)
#         else:
#             print("Head aega")
#     except :
#         print("Viga")
#except :
#    print("Viga")

#try:
#    alghind = float(input("Sisesta alghind: "))
#    if alghind>700:
        
#        protsent=30
        
#        summa=(protsent/100)*alghind 
        
#        hind=alghind-summa 
        
#        print(f"30% soodustusega hind on " + str(hind) + "eurot.")
#    else:
#        print(f"alghind peab olema suurem kui 700 eurot, et sada 30% soodustust.")
       
#except :
#    print("Vigane sisend. palun sisesta arvuline väärtus.")



#try:
#    print("Здравствуйте!")
   
#    nimi = input("Введите свое имя: ")
   
   
#    print(nimi + ", Красивое имя!")
   
   
#    vastus = int(input(nimi + "! Могу ли я найти твой индекс массы тела? 0 - нет, 1 - да => "))
   
#    if vastus == 1:
#        try:
         
#            pikkus = int(input("Введи длину (в см): "))
           
           
#            mass = float(input("Введи вес (в кг): "))
           
           
#            indeks = mass / (0.01 * pikkus) ** 2
           
           
#            print(nimi + "! Твой индекс массы тела: {:.1f}".format(indeks))
           
           
#            if indeks < 16:
#                print("Опасный для здоровья недостаток веса")
#            elif 16 <= indeks < 19:
#                print("Недостаток веса")
#            elif 19 <= indeks < 25:
#                print("Нормальный вес")
#            elif 25 <= indeks < 30:
#                print("Избыточный вес")
#            elif 30 <= indeks < 35:
#                print("Ожирение")
#            elif 35 <= indeks < 40:
#                print("Тяжёлое ожирение")
#            else:
#                print("Ожирение, представляющее опасность для здоровья")
       
#        except ValueError:
#            print("Ошибка! Пожалуйста, введите подходящие числа.")
   
#    else:
#        print("Жаль! Это очень полезная информация!")
#        print()

#    print("До свидания, " + nimi + "!")

#except ValueError:
#    print("Ошибка! Пожалуйста, введите подходящие числа.")


#korrutamine=5
#for i in range(1,11):          #9
#    tulemus =(i)*5
#    print(f"{i}* 5 = {tulemus}")

#import random

#def Начать_игру():
#    print("Я загадал число от 1 до 100.")
#    число_к = random.randint(1, 100)
#    ввод_п = ""

#    while ввод_п != "конец":
#        ввод_п = input("Угадай число (или введите 'конец' чтобы закончить) ")

#        if ввод_п == "конец":
#            print(f"Игра завершена. Правильное число было {число_к}.")
#            break

#        число_п = int(ввод_п)

#        if число_п < число_к:
#            print("Число больше, попробуйте еще раз.")
#        elif число_п > число_к:
#            print("Число меньше, попробуйте еще раз.")
#        else:
#            print(f"Правильное число! Это было {число_к}. Игра окончена.")
#            break

#if __name__ == "__main__":
#    Начать_игру()
