def joueur() :






n = 10

while n>0:
  allumette =-1
  while allumette <1 or allumette>n or allumette>n:
    allumette = int(input("combien d'allumettes prenez-vous ?"))
    n = n - allumette
    if n==0:
        print("vous avez perdu")
    else :
        print("il reste", n)
        if n%4==3:
            p=2
        elif n%4==2:
            p=1
        elif n%4==0:
            p=3
        else:
            p=1
        print("j'en prends", p)
        n=n-p
        print("il en reste", n)
        if n==0:
            print("j'ai perdu")
