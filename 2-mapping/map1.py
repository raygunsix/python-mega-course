import folium
import os

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2,-99.1],[37.2,-100.1]]:
    fg.add_child(folium.Marker(location=coordinates,popup="I'm a marker!",icon=folium.Icon(color="green")))

map.add_child(fg)

map.save(os.path.expanduser('~/Desktop/map1.html'))