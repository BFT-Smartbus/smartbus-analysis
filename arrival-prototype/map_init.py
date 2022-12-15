import folium as fl
import pandas as pd

data = pd.read_csv("Heartbeats.csv")
lat = list(data["latitude"])
lon = list(data["longitude"])

heartbeats = []

for lt, ln in zip(lat, lon):
    heartbeats.append([lt, ln])

pickup_points = [
    heartbeats[57],
    heartbeats[102],
    heartbeats[168],
    heartbeats[212],
    heartbeats[281],
    heartbeats[312],
    heartbeats[-1],
]

m = fl.Map(location=[18.02, -76.80], zoom_start=14)

fg_heartbeat = fl.FeatureGroup(name="Heartbeat data")
fg_start = fl.FeatureGroup(name="Start point")
fg_end = fl.FeatureGroup(name="End point")
fg_poly = fl.FeatureGroup(name="Polyline")
fg_pickup = fl.FeatureGroup(name="Pickup points")
fg_rad = fl.FeatureGroup(name="Radius geo-fence (NTS)")

for heartbeat in heartbeats:
    fg_heartbeat.add_child(fl.Marker(location=heartbeat))

for pickup in pickup_points:
    fg_rad.add_child(
        fl.CircleMarker(
            location=[*pickup],
            radius=30,
            fill_color="purple",
            opacity=0.7,
            color="purple",
        )
    )
    fg_pickup.add_child(fl.Marker(location=[*pickup], icon=fl.Icon(color="purple")))

fg_start.add_child(fl.Marker(location=[*heartbeats[0]], icon=fl.Icon(color="green")))
fg_end.add_child(fl.Marker(location=[*heartbeats[-1]], icon=fl.Icon(color="red")))
fg_poly.add_child(fl.PolyLine(locations=heartbeats))

m.add_child(fg_heartbeat)
m.add_child(fg_start)
m.add_child(fg_end)
m.add_child(fg_poly)
m.add_child(fg_pickup)
m.add_child(fg_rad)
m.add_child(fl.LayerControl())

m.save("map.html")
