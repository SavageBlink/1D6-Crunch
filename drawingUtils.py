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
                map.add_child(folium.Marker(location = point,
                tooltip = 'Arrival'))
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

    printable_cons = str(int(cons)) + "kWh"
    kwh_conv = 10.74 #1 litre de diesel = 10.74 kWh
    diesel_litre = cons/kwh_conv
    printable_diesel = "Soit " + str(int(diesel_litre)) + " litres de diesel"

    popup_content = printable_cons + "\n" + printable_diesel
    if(cons <= lower_cons):

        folium.PolyLine(couple,
        color="green",
        tooltip = printable_cons,
        popup = popup_content ,
        weight=4.5,
        opacity=1).add_to(map)

    elif(cons >= upper_cons):

        folium.PolyLine(couple,
         color="red",
         tooltip = printable_cons,
         popup = popup_content ,
         weight=4.5,
         opacity=1).add_to(map)

    if(cons > lower_cons and cons < upper_cons):

        folium.PolyLine(couple,
        color="#ff6a00",
        tooltip = printable_cons,
        popup = popup_content ,
        weight=4.5,
        opacity=1).add_to(map)
