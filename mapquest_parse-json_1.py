books api key
cisco|S8LjbCN28kqoYRXX0XZzK9S0qw3S2uWZqTb71AbCT6A

map quest api key
fatOUKlbBcdAuMLqejBbOJFVjQ1yCfeL


import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "fatOUKlbBcdAuMLqejBbOJFVjQ1yCfeL"
while True:
    print("Ingrese ciudad con el Siguiente Formato 'Ciudad, País', Si desea Salir Escriba 'q'")
    orig = input("Ciudad de Origen: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Ciudad de Destino: ")
    if orig == "quit" or orig == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direccion origen desde " + (orig) + " hacia " + (dest))
        print("Duracion Del Viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
