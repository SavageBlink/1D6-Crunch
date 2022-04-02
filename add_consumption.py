from mmparsing import *
import math


# Take an array with all the consumptions as a parameter
# Append this consumption at the end of each line in the file path_of_output_file
# -> change 2 file paths if necessary
def add_consumption(consumption):


    path_of_reading_file = "consommation_jeu_de_donnee.txt"
    path_of_output_file = "Data/jeu_de_donne_avec_conso.txt"
    is_arc = False
    i = 0
    with open(path_of_reading_file, 'r') as istr:
        with open(path_of_output_file, 'w') as ostr:
            for line in istr:
                if line == "Arcs\n":
                    is_arc = True
                    continue
                if is_arc:  # If it's an arc, we add the consumption at the end
                    line = line.rstrip('\n') + str(consumption[i])
                    print("ok")
                    ++i
                    print(line, file=ostr)


# Return the calculation of the consumption by using a formula and parse functions
def consumption_calculation():
    data = Parsing("Data/jeu_de_donee_sans_conso.txt")
    v = data["speed"]
    d = Parsing["distance"]
    p = Parsing["pente"]  # A METTRE EN RADIANT
    m = 1000  # default mass
    number_of_archs = len(d)
    consumption = []

    for i in range(number_of_archs):
        print(i)
        # consumption[i] = (0.196*v[i]*v[i] + 73.6*m[i] + 9.81*m[i]*math.tan(p[i])*d[i]) / (3.6*pow(10, 5))  # résultat en kwH
        consumption.append(2)

    return consumption


# Conso à initialiser avec le parsing du fichier et la formule
add_consumption(consumption_calculation())

