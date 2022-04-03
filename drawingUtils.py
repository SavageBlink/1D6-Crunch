import folium
import jinja2

def drawMap(points_tupple,cons_arcs = None,lower_cons=None,upper_cons=None):

    print(points_tupple)
    ave_lat = sum(p[0] for p in points_tupple)/len(points_tupple)
    ave_lon = sum(p[1] for p in points_tupple)/len(points_tupple)

    map = folium.Map(location=[ave_lat, ave_lon], zoom_start=9)



    """
    Drawing points from input tupple
    """
    drawPoints(map,points_tupple,cons_arcs,lower_cons,upper_cons)
    saveMap(map)

def saveMap(map,filename = None):
    path = "map/"
    if(filename != None):
        path+=filename
    else:
        path+="index.html"

    map.save(path)

def drawPoints(map,points_tupple,cons_arcs = None,lower_cons=None,upper_cons=None):

        for point in points_tupple:
            p_index = points_tupple.index(point)


            """Drawing first marker as Departure"""
            if(p_index == 0):
                map.add_child(folium.Marker(location = point,
                tooltip = 'Departure'))
                """Drawing last marker as Arrival"""
            elif(p_index == len(points_tupple)-1):
                f_cons = 0
                for cons in cons_arcs:
                    f_cons+=cons
                f_cons = "{:.2f}".format(f_cons)
                printable_cons = str(f_cons) + "kWh"

                kwh_conv = 10.74 #1 litre de diesel =~ 10.74 kWh
                eur_conv = 2.14 #1 litre de diesel = 2.14€

                diesel_litre = cons/kwh_conv
                diesel_eur = diesel_litre * eur_conv

                diesel_litre = "{:.2f}".format(diesel_litre)
                diesel_eur = "{:.2f}".format(diesel_eur)

                printable_diesel = str(diesel_litre) + " L"
                printable_eur = str(diesel_eur) + "€"

                popup_content = "Arrival" + "\n" +printable_cons + "\n" + printable_diesel + "\n" + printable_eur
                map.add_child(folium.Marker(location = point,
                popup = popup_content ))
                """Drawing inner arcs points as red dots"""
            else:
                map.add_child(folium.CircleMarker(location = point,
                fill = 'true',
                radius = 3,
                fill_color='yellow',
                color = 'clear',
                fill_opacity = 1))

            if((p_index != len(points_tupple) - 1) and cons_arcs != None):
                cons = cons_arcs[p_index]
                drawLine(map,[point,points_tupple[p_index + 1]],cons,lower_cons,upper_cons)

                """            if(p_index != len(points_tupple) - 1):

                                print(points_tupple[p_index + 1])
                                p_nxt = points_tupple[p_index + 1]

                                folium.PolyLine([point,p_nxt],color="blue",weight=4.5).add_to(map)"""

def drawLine(map,couple,cons,lower_cons,upper_cons):
    n_cons = "{:.2f}".format(cons)
    printable_cons = str(n_cons) + "kWh"
    kwh_conv = 10.74 #1 litre de diesel =~ 10.74 kWh
    eur_conv = 2.14 #1 litre de diesel = 2.14€

    diesel_litre = cons/kwh_conv
    diesel_eur = diesel_litre * eur_conv

    diesel_litre = "{:.2f}".format(diesel_litre)
    diesel_eur = "{:.2f}".format(diesel_eur)

    printable_diesel = str(diesel_litre) + " L"
    printable_eur = str(diesel_eur) + "€"

    popup_content = printable_cons + "\n" + printable_diesel + "\n" + printable_eur
    if(cons <= lower_cons):

        folium.PolyLine(couple,
        color="green",
        tooltip = printable_cons,
        weight=4.5,
        opacity=1).add_to(map)

    elif(cons >= upper_cons):

        folium.PolyLine(couple,
         color="red",
         tooltip = printable_cons,
        weight=4.5,
         opacity=1).add_to(map)

    if(cons > lower_cons and cons < upper_cons):

        folium.PolyLine(couple,
        color="#ff6a00",
        tooltip = printable_cons,
        weight=4.5,
        opacity=1).add_to(map)
