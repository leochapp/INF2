import googlemaps

class Gmap:
    def coordgps(adresse):
        gmaps = googlemaps.Client(key='AIzaSyBTeRxf61DWGHagCM2SOVupUhdo2POEkxE')
        geocode_result = gmaps.geocode(adresse)
        lat = geocode_result[0]["geometry"]["location"]["lat"]
        lng = geocode_result[0]["geometry"]["location"]["lng"]
    return lat,lng



class Lieu():

    def __init__(self):
        self.nom = str(input("Veuillez rentrer votre nom : "))
        self.adresse = str(input("Veuillez rentrer une adresse : "))
        self.latitude = str(input("Veuillez rentrer une latitude : "))
        self.longitude = str(input("Veuillez rentrer une longitude : "))
