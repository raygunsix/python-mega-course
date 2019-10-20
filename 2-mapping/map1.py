import folium
import os
import pandas

volcanoes = pandas.read_csv("volcanoes.csv")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])

def elevation_style(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58,-99.09],zoom_start=6,tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el) + " m",stroke=True,color="grey",fill=True,fill_opacity=0.7,fill_color=elevation_style(el)))

map.add_child(fg)

map.save(os.path.expanduser("~/Desktop/map1.html"))