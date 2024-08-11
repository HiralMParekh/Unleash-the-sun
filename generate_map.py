import folium
from  flask import redirect
# Example coordinates
coordinates = [.022523, 72.5714, 23.0345, 72.5563, 23.0111, 72.5984]

# Convert coordinates to a list of [latitude, longitude] pairs
house_coordinates = [[coordinates[i], coordinates[i+1]] for i in range(0, len(coordinates), 2)]

# Create a map centered at the first coordinate
map = folium.Map(location=house_coordinates[0], zoom_start=14)

# Add a polygon to the map
folium.Polygon(
    locations=house_coordinates,
    color='blue',
    fill=True,
    fill_color='blue',
    fill_opacity=0.5
).add_to(map)

# Save the map to an HTML file
map.save('leaflet_map.jpeg')
return redirect(url_for(i))
