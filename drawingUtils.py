import folium


def drawMap(points_tupple,cons_arcs = None,lower_cons=None,upper_cons=None):

    my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=9)

    blue_icon = folium.CustomIcon(r"asset\icon\blue_icon.png")
    """
    Drawing points from input tupple
    """
    drawPoints(points_tupple,cons_arcs,lower_cons,upper_cons)    
    saveMap(my_map)

def saveMap(map,filename = None):
    path = "map/"
    if(filename != None):
        path+=filename
    else:
        path+="index.html"

    map.save(path)

def drawPoints(points_tupple,cons_arcs = None,lower_cons=None,upper_cons=None):

        for point in points_tupple:
            p_index = points_tupple.index(point)


            """Drawing first marker as Departure"""
            if(p_index == 0):
                my_map.add_child(folium.Marker(location = point,
                tooltip = 'Departure'))
                """Drawing last marker as Arrival"""
            elif(p_index == len(points_tupple)-1):
                my_map.add_child(folium.Marker(location = point,
                tooltip = 'Arrival'))
                """Drawing inner arcs points as red dots"""
            else:
                my_map.add_child(folium.CircleMarker(location = point,
                fill = 'true',
                radius = 3,
                fill_color='yellow',
                color = 'clear',
                fill_opacity = 1))

"""            if(p_index != len(points_tupple) - 1):

                print(points_tupple[p_index + 1])
                p_nxt = points_tupple[p_index + 1]

                folium.PolyLine([point,p_nxt],color="blue",weight=4.5).add_to(my_map)"""


            if(p_index != len(points_tupple)-1 and cons_arcs != None):
                cons = cons_arcs[p_index]
                drawLine(map,[point,points_tupple[p_index + 1]])

def drawLine(map,couple,cons,lower_cons,upper_cons):

    printable_cons = str(cons) + "kWh"

    if(cons <= lower_cons):

        folium.PolyLine(couple,
        color="green",
        tooltip = printable_cons,
        popup = printable_cons ,
        weight=4.5,
        opacity=1).add_to(map)

    elif(cons >= upper_cons):

        folium.PolyLine(couple,
         color="red",
         tooltip = printable_cons,
         popup = printable_cons ,
         weight=4.5,
         opacity=1).add_to(map)

    if(cons > lower_cons and cons < upper_cons):

        folium.PolyLine(couple,
        color="#ff6a00",
        tooltip = printable_cons,
        popup = printable_cons ,
        weight=4.5,
        opacity=1).add_to(map)
