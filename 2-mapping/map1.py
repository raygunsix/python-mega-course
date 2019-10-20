import folium
import os
import pandas

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles = "Stamen Terrain")
volcanoes = pandas.read_csv("volcanoes.csv")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln],popup="I'm a marker!",icon=folium.Icon(color="green")))

map.add_child(fg)

map.save(os.path.expanduser("~/Desktop/map1.html"))