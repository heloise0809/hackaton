import numpy as np

def creer_pyramide():
    pyramide = np.array([])
    n=0
    while(n != "q"):
        n = int(input("Entrez le nombre d'allumettes souhaitez pour cette etage(entrez q pour stop):"))
        ones=np.ones(n)
        pyramide= np.concatenate((pyramide, ones), axis=0)
        print(pyramide)


if __name__ == '__main__':
    #creer_pyramide()
    pyramide = np.array([[1], [1, 1], [1, 1, 1]])
    for i in range(0, len(pyramide)):
        print pyramide[i]

    while(len(pyramide) != 0):
        ligne = input("Entrez le numero de ligne ")
        n = input("Entrez le nombre d'allumettes a supprimer: ")


        if n >= len(pyramide[ligne]):
            pyramide = np.delete(pyramide, ligne, axis=0)
            print pyramide
            continue

        # position du premier 1 a droite sur la ligne
        i=len(pyramide[ligne])-1
        while i>0:
            while pyramide[ligne][i]==0:
                i = i-1
                continue
            nbre_allumettes=i+1
            #si nombre d'allumettes restants > nbre allumettes a supprimer
            if n >= nbre_allumettes:
                pyramide = np.delete(pyramide, ligne, axis=0)
                print pyramide
                break
            #si la derniere allumettes va etre supprime
            if pyramide[ligne][i]==1 and i==0:
                pyramide = np.delete(pyramide, ligne, axis=0)
                print pyramide
                break

            pyramide[ligne][i]=0
            i=i-1
            n=n-1


            print pyramide