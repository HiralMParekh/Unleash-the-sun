from flask import Flask, request, render_template, send_file
import folium
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('data.html')

@app.route('/generate-map', methods=['POST'])
def generate_map():
    coordinates_str = request.form.get('coordinates')
    
    if not coordinates_str:
        return 'No coordinates provided.', 400
    
    try:
        coordinates = [float(coord) for coord in coordinates_str.split(',')]
        if len(coordinates) % 2 != 0:
            return 'The number of coordinates should be even (latitude, longitude pairs).', 400

        house_coordinates = []
        for i in range(0, len(coordinates), 2):
            house_coordinates.append([coordinates[i], coordinates[i+1]])

        # Create a Folium map centered at the first coordinate
        map = folium.Map(location=house_coordinates[0], zoom_start=20, max_zoom=20, min_zoom=20)

        # Add a polygon to the map
        folium.Polygon(
            locations=house_coordinates,
            color='blue',
            fill=True,
            fill_color='blue',
            fill_opacity=0.5
        ).add_to(map)
        
        # Save the map to an HTML file
        map_file = 'leaflet_map.html'
        map.save(map_file)
        
        # Serve the HTML file for download
        return send_file(map_file, as_attachment=True)

    except ValueError:
        return 'Invalid coordinates format.', 400

if __name__ == '__main__':
    app.run(debug=True)
