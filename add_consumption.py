
# Take an array with all the consumptions as a parameter
# Append this consumption at the end of each line in the file path_of_output_file
# -> change 2 file paths if necessary
def add_consumption(consumption):
    # For test purpose :
    consumption = [3 for i in range(8)]


    path_of_reading_file = "Data/jeu_de_donne_test_sans_conso.txt"
    path_of_output_file = "Data/jeu_de_donne_test_avec_conso.txt"
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


conso = []
add_consumption(conso)
