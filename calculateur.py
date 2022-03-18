
#! Coef = 1
#TODO : Ajouter les coeficients pour les prendres en compte dans la moyenne
n_liste = []
run = True
while run :
    note = input("Entrer votre note :")
    if note == "" :
        run = False
    else :
        n_liste.append(eval(note))

moyenne = sum(n_liste) / len(n_liste)

print("La moyenne de toute les notes entrées est {}.".format(moyenne))