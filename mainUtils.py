import parse
import optimise

def getOptimisedPath(start_point,end_point,filename=None):
    points = []
    cons_arcs = []

    if(filename == None):
        filename = "consommation_jeu_de_donnee.txt"

    formated = optimise.formatOptimise(start_point,end_point,filename)

    for tupple in formated:
        points.append(parse.getCoordFromNodeParsing(tupple[0],filename))
        cons_arcs.append(tupple[2])

    return [points,cons_arcs]
