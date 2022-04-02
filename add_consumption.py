from parse import *

import math


# Take an array with all the consumptions as a parameter
# Append this consumption at the end of each line in the file path_of_output_file
# -> change 2 file paths if necessary
def add_consumption(consumption):

    path_of_reading_file = "Data/jeu_de_donne_sans_conso.txt"
    path_of_output_file = "Data/jeu_de_donne_avec_conso.txt"
    is_arch = False
    i = 0
    with open(path_of_reading_file, 'r') as istr:
        with open(path_of_output_file, 'w') as ostr:
            for line in istr:
                if line == "Arcs:\n":
                    is_arch = True
                    continue
                if is_arch:  # If it's an arc, we add the consumption at the end
                    line = line.rstrip('\n') + str(consumption[i])
                    print(i)
                    i+=1
                    print(line, file=ostr)


# Return the calculation of the consumption by using a formula and parse functions
def consumption_calculation():
    data = Parsing("consommation_jeu_de_donnee.txt")
    v = [float(x) for x in data["speed"]]
    d = [float(x) for x in data["distance"]]
    p = [float(x) for x in data["pente"]]  # A METTRE EN RADIANT
    # consumption = [float(x) for x in parsed["consommation"]]
    m = 1000.0  # default mass
    number_of_archs = len(d)
    consumption = []

    for i in range(number_of_archs):
        one_data = (0.196*v[i]*v[i] + 73.6*m + 9.81*m*math.tan(p[i])) * 2*d[i] / (3.6*pow(10, 5))
        #print(one_data)
        consumption.append(one_data)  # résultat en kwH



    return consumption


# Conso à initialiser avec le parsing du fichier et la formule
#add_consumption(consumption_calculation())
add_consumption(consumption_calculation())

