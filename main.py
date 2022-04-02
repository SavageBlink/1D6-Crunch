import drawingUtils
import parse
import optimise
from consumption import *

# Generate consumption data
add_consumption(consumption_calculation())

# Generate file with energy consumption




points_a = [[1,50], [1.2,50.3], [1.23, 50.7],[1,50.3]]
points_b = [[3,60], [2.2,60.3], [2.23, 51.7],[2,51.3]]
cons_arcs_b = [200,100,500]
upper_cons = 250
lower_cons = 140
limit_cons = [lower_cons,upper_cons]
# Load map centred on average coordinates
ave_lat = sum(p[0] for p in points_b)/len(points_b)
ave_lon = sum(p[1] for p in points_b)/len(points_b)


"""points_x_coordinates = mmparsing.Parsing("CoordinateX","test.txt")
points_y_coordinates = mmparsing.Parsing("CoordinateY","test.txt")"""



"""def getPoints():
    points_test = []
    for i in range(len(points_x_coordinates)):
        point = [float(points_x_coordinates[i]),float(points_y_coordinates[i])]
        points_test.append(point)
        #print(points_test[i])
    return points_test

points_test = getPoints()"""

points = []

formated = optimise.formatOptimise(1,200,"consommation_jeu_de_donnee.txt")

for tupple in formated:
    points.append(parse.getCoordFromNodeParsing(tupple[0],"consommation_jeu_de_donnee.txt"))
    #points.append(parse.getCoordFromNodeParsing(tupple[1],"consommation_jeu_de_donnee_faux.txt"))
    print(tupple[0],tupple[1])


cons_arcs = []

for tupple in formated:
    cons_arcs.append(tupple[2])
    print(tupple[2])

drawingUtils.drawMap(points,cons_arcs,30,70)



# add lines
#folium.PolyLine(points_a, color="blue", weight=1.5, opacity=1).add_to(my_map)


# Save map
