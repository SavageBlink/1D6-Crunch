import parse
import optimise
import consumption

def getOptimisedPath(start_point,end_point,filename=None):
    points = []
    cons_arcs = []

    if(filename == None):
        filename = "consommation_jeu_de_donnee.txt"

    formated = optimise.formatOptimise(start_point,end_point,filename)

    print("formated : ",formated)

    for tupple in formated:
        points.append(parse.getCoordFromNodeParsing(tupple[0],filename))
        cons_arcs.append(tupple[2])
        if(formated.index(tupple) == len(formated)-1):
            points.append(parse.getCoordFromNodeParsing(tupple[1],filename))

    return [points,cons_arcs]

def computeConsumption(input,output = None):
    if(output == None):
        output = input
    cons = consumption.consumption_calculation(input)
    return consumption.add_consumption(cons,input,output)
