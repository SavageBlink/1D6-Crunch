
def Parsing(sFile):
    #Initialisation variables
    NombreNoeuds = 0
    Coordonnee = [[], []]
    Coor = 0
    noeud = [[], []]
    distance = []
    vitesse = []
    pente = []
    consommation = []
    #Create a dictionnary
    data = {"CoordinateX": Coordonnee[0], "CoordinateY": Coordonnee[1], "noeudStart": noeud[0] , "noeudEnd": noeud[1],
            "distance": distance, "speed": vitesse, "pente": pente, "consommation": consommation}
    #open the consommation file
    with open(sFile, 'r') as f:
        for line in f:
            #Récupère la vaaleur de la ligne
            Value = line.strip()            #correspond aux valeurs présentent dans le bloc note
            #Si Value n'est pas une ligne vide
            if Value != "":
                #Si Value contient "Arcs"
                if "Arcs:" in Value:
                    Coor = 1
                    continue
                if Coor == 0:
                    # Valeur.split(caractère de séparation, nombre de séparation)[indice]
                    Coordonnee[0].append(Value.split(";", 3)[1])
                    Coordonnee[1].append(Value.split(";", 3)[2])
                    NombreNoeuds = NombreNoeuds + 1
                else :
                    noeud[0].append(Value.split(";", 5)[0])
                    noeud[1].append(Value.split(";", 5)[1])
                    distance.append(Value.split(";", 5)[2])
                    vitesse.append(Value.split(";", 5)[3])
                    pente.append(Value.split(";", 5)[4])
                    consommation.append(Value.split(";", 5)[5])




#    for y in range(0, 25000):
#        print(distance[y])
    return data


def RechercheNoeud(CoordonneeX1, CoordonneeY1):

    DonneeParsing = Parsing("consommation_jeu_de_donnee.txt")
    NombreNoeuds = len(DonneeParsing["CoordinateX"])

    for y in range(0, NombreNoeuds):
            if(CoordonneeX1 == float(DonneeParsing["CoordinateX"][y])):
                if(CoordonneeY1 == float(DonneeParsing["CoordinateY"][y])):

                    Noeud = y
                break

    return Noeud + 1


Noeud1 = RechercheNoeud(24.1472, 17.9533)
#Noeud2 = RechercheNoeud(23.6731, 19.0991)
print(Noeud1)


