# Created by Andrew Willard
# 20250313

import tkinter as tk # https://www.geeksforgeeks.org/python-gui-tkinter/
import tkintermapview # https://github.com/TomSchimansky/TkinterMapView

root_tk = tk.Tk()
root_tk.geometry(f"{700}x{600}")
root_tk.title("CT FastTrack Map")

map_widget = tkintermapview.TkinterMapView(root_tk, width=700, height=500, corner_radius=0)

map_widget.pack(fill="both", expand=True)

# set current widget position and zoom
mapCenterStartingLat = 41.721987
mapCenterStartingLon = -72.7188110
# Convert to float, handling potential errors
try:
    mapCenterStartingLat = float(mapCenterStartingLat)
    mapCenterStartingLon = float(mapCenterStartingLon)
except ValueError:
    print("Invalid latitude or longitude value")
    # Handle the error appropriately, e.g., use default values or exit
    mapCenterStartingLat = 0.0
    mapCenterStartingLon = 0.0
map_widget.set_position(mapCenterStartingLat, mapCenterStartingLon)
map_widget.set_zoom(12)

latBOC , lonBOC = 41.784147 , -72.655601 # BOC
latAmtrakOverpassSB2 , lonAmtrakOverpassSB2 = 41.779859 , -72.664398 # AmtrakOverpassSB2
latMarketStSB1 , lonMarketStSB1 = 41.769601 , -72.670801 # MarketStSB1
latAsylumStUnionStation , lonAsylumStUnionStation = 41.767887 , -72.681916 # AsylumStUnionStation
latFlowerSt , lonFlowerSt = 41.765819 , -72.687950 # FlowerSt
latSigourneyStStation , lonSigourneyStStation = 41.764421 , -72.695020 # SigourneyStStation
latI84Cam , lonI84Cam = 41.761343 , -72.700044 # I84Cam
latParkvilleStation , lonParkvilleStation = 41.757179 , -72.704029 # ParkvilleStation
latHamiltonSt , lonHamiltonSt = 41.754758 , -72.705652 # HamiltonSt
latKaneStStation , lonKaneStStation = 41.750404 , -72.709222 # KaneStStation
latFlatbushAveStation , lonFlatbushAveStation = 41.741410 , -72.716399 # FlatbushAveStation
latOakwoodAve , lonOakwoodAve = 41.737050 , -72.719744 # OakwoodAve
latElmwoodStation , lonElmwoodStation = 41.731026 , -72.724846 # ElmwoodStation
latNewingtonJunctionStation , lonNewingtonJunctionStation = 41.716354 , -72.736512 # NewingtonJunctionStation
latCedarStStation , lonCedarStStation = 41.696143 , -72.753989 # CedarStStation
latCedarSt , lonCedarSt = 41.694109 , -72.754205 # CedarSt
latEastStStation , lonEastStStation = 41.687713 , -72.758884 # EastStStation
latSmalleySt , lonSmalleySt = 41.673947 , -72.764624 # SmalleySt
latEastMainStStationNB , lonEastMainStStationNB = 41.672099 , -72.765472 # EastMainStStationNB
latEastMainStStationSB , lonEastMainStStationSB = 41.671650 , -72.766354 # EastMainStStationSB
latDowntownNewBritainStation , lonDowntownNewBritainStation = 41.668703 , -72.779958 # DowntownNewBritainStation

"""
marker_1 = map_widget.set_marker(lat, lon, text="Vance")

def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="new marker")
"""

# Fasttrak locations
marker_1=map_widget.set_marker(latBOC,lonBOC, text="BOC")
marker_2=map_widget.set_marker(latAmtrakOverpassSB2,lonAmtrakOverpassSB2, text="Amtrak Overpass (splice box #2)")
marker_3=map_widget.set_marker(latMarketStSB1,lonMarketStSB1, text="Market Street  (splice box #1)")
marker_4=map_widget.set_marker(latAsylumStUnionStation,lonAsylumStUnionStation, text="Asylum Street / Union Station")
marker_5=map_widget.set_marker(latFlowerSt,lonFlowerSt, text="Flower Street")
marker_6=map_widget.set_marker(latSigourneyStStation,lonSigourneyStStation, text="Sigourney Street Station")
marker_7=map_widget.set_marker(latI84Cam,lonI84Cam, text="I-84 Cam")
marker_8=map_widget.set_marker(latParkvilleStation,lonParkvilleStation, text="Parkville Station")
marker_9=map_widget.set_marker(latHamiltonSt,lonHamiltonSt, text="Hamilton Street")
marker_10=map_widget.set_marker(latKaneStStation,lonKaneStStation, text="Kane Street Station")
marker_11=map_widget.set_marker(latFlatbushAveStation,lonFlatbushAveStation, text="Flatbush Avenue Station")
marker_12=map_widget.set_marker(latOakwoodAve,lonOakwoodAve, text="Oakwood Ave")
marker_13=map_widget.set_marker(latElmwoodStation,lonElmwoodStation, text="Elmwood Station")
marker_14=map_widget.set_marker(latNewingtonJunctionStation,lonNewingtonJunctionStation, text="Newington Junction Station")
marker_15=map_widget.set_marker(latCedarStStation,lonCedarStStation, text="Cedar Street Station")
marker_16=map_widget.set_marker(latCedarSt,lonCedarSt, text="Cedar Street")
marker_17=map_widget.set_marker(latEastStStation,lonEastStStation, text="East Street Station")
marker_18=map_widget.set_marker(latSmalleySt,lonSmalleySt, text="Smalley Street")
marker_19=map_widget.set_marker(latEastMainStStationNB,lonEastMainStStationNB, text="East Main Street Station (Northbound)")
marker_20=map_widget.set_marker(latEastMainStStationSB,lonEastMainStStationSB, text="East Main Street Station (Southbound)")
marker_21=map_widget.set_marker(latDowntownNewBritainStation,lonDowntownNewBritainStation, text="Downtown New Britain Station")

"""
# set a path
path_1 = map_widget.set_path([marker_2.position, marker_3.position, (52.57, 13.4), (52.55, 13.35)])

# methods
path_1.set_position_list(new_position_list)
path_1.add_position(position)
path_1.remove_position(position)
path_1.delete()

# Set the initial position of the map
map_widget.set_position(52.57, 13.4)  # Change this to a suitable starting point
map_widget.set_zoom(12)
"""

# Create a path with the markers
positions = [
    marker_1.position, marker_2.position, marker_3.position,
    marker_4.position, marker_5.position, marker_6.position,
    marker_7.position, marker_8.position, marker_9.position,
    marker_10.position, marker_11.position, marker_12.position,
    marker_13.position, marker_14.position, marker_15.position,
    marker_16.position, marker_17.position, marker_18.position,
    marker_19.position, marker_20.position, marker_21.position
]

# Set the path from the list of positions
path_1 = map_widget.set_path(positions)

"""
# You can modify the path by adding or removing positions
path_1.add_position((52.47, 13.53))  # Example of adding a new position to the path
path_1.remove_position(marker_10.position)  # Example of removing a position from the path
"""


"""
# Function to print out path info
def print_path_info():
    print("Current path positions:")
    for position in path_1.get_position_list():
        print(position)

# Button to print path info
path_button = tk.Button(root, text="Print Path Info", command=print_path_info)
path_button.pack()
"""


"""
def add_marker_event(coords):
    print("Add marker:", coords)
    new_marker = map_widget.set_marker(coords[0], coords[1], text="")
map_widget.add_right_click_menu_command(label="Add Marker",command=add_marker_event,pass_coords=True)
"""
root_tk.mainloop()