def on_suuremaid(jarjend, piir):
  return max(jarjend) > piir

tabel = [[1, -43, 5, 3, 7], [-4, 6, 7, 9, 8], [5, 6, -7, -1, 4]]

loendaja = 0
for el in tabel:
 if on_suuremaid(el, 6):
  loendaja += 1

print(loendaja)



#from Module import *
#from random import *

##2
#vastus= is_year_leap(int(input("Aasta:")))
#if vastus:
#    print("Liigaasta")
#else:
#    print("TAvaline aasta")



#a=[]
#b=[]
##(1) arithmetic()
#v=arithmetic(float(input("Arv1: ")), float(input("Arv2: ")),input("Operatsion: "))
#print(v)

#for i in range(5):
#    a.append(randint(-20, 20))
#for i in range(1, 4):
#    arv=int(input(f"{i}. arv"))
#    b.append(arv)
#print(a)
#print(b)
#print()
#Suurim_element(a, b)


#a=randint(-10, 10)
#print("Esimene arv=", a)
#b=float(input("Teine arv:"))
#kor=Korrutis(a,b,5.5)
#print("Tulemus: ", kor)
#kor=Korrutis(b,a,b,10)
#print(f"Tulemus: {b}*{a}*{b}*10=", kor)