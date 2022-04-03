from parse import *
from global_variable import *
import math


# Take an array with all the consumptions as a parameter
# Append this consumption at the end of each line in the file path_of_output_file
# -> change 2 file paths if necessary
def add_consumption(consumption,input,output = None):

    path_of_reading_file = input
    if(output == None):
        output = input
    path_of_output_file = output
    is_arch = False
    i = 0
    with open(path_of_reading_file, 'r') as istr:
        with open(path_of_output_file, 'w') as ostr:
            for line in istr:
                Value = line.strip()            #correspond aux valeurs présentent dans le bloc note
                #Si Value n'est pas une ligne vide
                if Value != "":
                    if line == global_arch_data_separator:
                        is_arch = True
                        print("Arcs:", file=ostr)
                        continue
                    if is_arch:  # If it's an arc, we add the consumption at the end
                        line = line.rstrip('\n') + str(consumption[i])
                        i+=1
                        print(line, file=ostr)
                    else:
                        print(line.rstrip('\n'), file=ostr)


# Return the calculation of the consumption by using a formula and parse functions
def consumption_calculation(filename):
    data = Parsing(filename)
    v = [float(x) for x in data["speed"]]
    d = [float(x) for x in data["distance"]]
    p = [float(x)*math.pi/180 for x in data["pente"]]  # A METTRE EN RADIANT
    # consumption = [float(x) for x in parsed["consommation"]]
    m = global_mass  # default mass
    number_of_archs = len(d)
    consumption = []

    for i in range(number_of_archs):
        one_data = (0.196*v[i]*v[i] + 73.6*m + 9.81*m*math.tan(p[i])) * 2*d[i] / (3.6*pow(10, 5))
        #print(one_data)
        consumption.append(one_data)  # résultat en kwH

    return consumption
