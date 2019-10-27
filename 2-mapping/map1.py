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

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln],popup=str(el) + " m",
    stroke=True,color="grey",fill=True,fill_opacity=0.7,fill_color=elevation_style(el)))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
    else 'orange' if 100000000 <= x['properties']['POP2005'] < 200000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl())

map.save(os.path.expanduser("~/Desktop/map1.html"))