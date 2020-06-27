import numpy as np
#def allumettes(nbre, etages):


if __name__ == '__main__':
    #n=input("Entrez le nombre d'allumettes")
    #etages = input("Entrez le nombre d'allumettes")

    pyramide = np.array([[1], [1, 1], [1, 1, 1]])
    for i in range(0, len(pyramide)):
        print pyramide[i]

    ligne = input("Entrez le numero de ligne ")
    n = input("Entrez le nombre d'allumettes a supprimer: ")

    for i in range(0, n):
        if i==len(pyramide[ligne]):
            pyramide=np.delete(pyramide, ligne, axis=0)
            break
        pyramide[ligne][i]=0

    print pyramide