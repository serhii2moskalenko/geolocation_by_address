from flask import Flask, render_template, request
import webbrowser
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="my_geocoder")


class GeocoderApp:
    def __init__(self):
        self.latitude = None
        self.longitude = None
        self.error = False

    def geocode_address(self, address):
        location = geolocator.geocode(address, language="ru")
        if location is not None:
            self.latitude = location.latitude
            self.longitude = location.longitude
            map_url = f"https://www.openstreetmap.org/?mlat={self.latitude}&mlon={self.longitude}&zoom=15"
            webbrowser.open(map_url)
        else:
            self.error = True


@app.route('/', methods=['GET', 'POST'])
def index():
    app = GeocoderApp()

    if request.method == 'POST':
        address = request.form['address']
        app.geocode_address(address)
        if not app.error:
            return render_template('index.html', success=True, original_address=address, latitude=app.latitude,
                                   longitude=app.longitude)
        else:
            return render_template('index.html', error=True)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
