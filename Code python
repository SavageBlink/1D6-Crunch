

# Un autre moyen de lire un fichier
#Initialisation variables
i = 0;
Coordonnee = [[], []]
Coor = 0
noeud = [[], []]
distance = []
vitesse = []
pente = []
consommation = []
with open("consommation_jeu_de_donnee.txt", 'r') as f:
    for line in f:
        Value = line.strip()            #correspond aux valeurs présent dans le bloc note
        #Valeur.split(caractère de séparation, nombre de séparation)[indice]
        if "Arcs" in Value:
            Coor = 1;
            continue
        if Coor == 0:
            Coordonnee[0].append(Value.split(";", 3)[1])
            Coordonnee[1].append(Value.split(";", 3)[2])
        else :
            noeud[0].append(Value.split(";", 5)[0])
            noeud[1].append(Value.split(";", 5)[1])
            distance.append(Value.split(";", 5)[2])
            vitesse.append(Value.split(";", 5)[3])
            pente.append(Value.split(";", 5)[4])
            consommation.append(Value.split(";", 5)[5])

        i = i+1;


f.close()
for y in range(0,1000):
    print(consommation[y])

