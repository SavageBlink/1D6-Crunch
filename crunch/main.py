import folium


points_a = [[1,50], [1.2,50.3], [1.23, 50.7],[1,50.3]]
points_b = [[3,60], [2.2,60.3], [2.23, 51.7],[2,51.3]]
cons_arcs_b = [200,100,500]
upper_cons = 250
lower_cons = 140
limit_cons = [lower_cons,upper_cons]
# Load map centred on average coordinates
ave_lat = sum(p[0] for p in points_b)/len(points_b)
ave_lon = sum(p[1] for p in points_b)/len(points_b)
my_map = folium.Map(location=[ave_lat, ave_lon], zoom_start=9)



def drawPoints(points_tupple,cons_arcs,lower_cons,upper_cons):

    blue_icon = folium.CustomIcon(r"asset\icon\blue_icon.png")
    """
    Drawing points from input tupple
    """

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

        if(p_index != len(points_tupple)-1):
            cons = cons_arcs[p_index]
            printable_cons = str(cons) + "kWh"

            if(cons <= lower_cons):
                folium.PolyLine([point,points_tupple[p_index+1]], color="green",tooltip = printable_cons,popup = printable_cons , weight=4.5, opacity=1).add_to(my_map)
            elif(cons >= upper_cons):
                folium.PolyLine([point,points_tupple[p_index+1]], color="red",tooltip = printable_cons,popup = printable_cons ,weight=4.5, opacity=1).add_to(my_map)
            if(cons > lower_cons and cons < upper_cons):
                folium.PolyLine([point,points_tupple[p_index+1]], color="#ff6a00",tooltip = printable_cons,popup = printable_cons , weight=4.5, opacity=1).add_to(my_map)


drawPoints(points_b,cons_arcs_b,lower_cons,upper_cons)

# add lines
#folium.PolyLine(points_a, color="blue", weight=1.5, opacity=1).add_to(my_map)


# Save map
my_map.save("./index.html")
