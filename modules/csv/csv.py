import json
import csv


# Permet de rechercher une ville dans le csv
# @param villeRecherche: String name of the city
# @return csvCity: array contain data of city
def recherche(villeRecherche):
    with open('Alentours de Toulouges.csv', newline='') as f:
        tableau = []
        csvCity = []
        lire = csv.reader(f)
        for ligne in lire:
            tableau.append(ligne)
            if ligne[0] == villeRecherche:
                if len(csvCity) < 40:
                    data = ligne[1].split(";")
                    dic = {"ville": ligne[0], "pays": data[0], "date": data[1], "temp": data[2], "min": data[3],
                           "max": data[4]}
                    csvCity.append(dic)
    jsondata = json.dumps(csvCity, sort_keys=True, indent=4).encode("utf8")
    copieJson(jsondata)
    return csvCity

# Permet d'enregistrer dans un fichier json
# @param tab: json
def copieJson(tab):
    fichier = open("json.json", "wb")
    fichier.write(tab)
    fichier.close()
    print("Copie Json Terminée")


# Permet d'ecrire dans un fichier csv
def copie(multiForecast_city):
    entetes = [
        u'Ville',
        u'Temp',
        u'Min',
        u'Max',
        u'Date'
    ]
    f = open('data.csv', 'w')
    ligneEntete = ";".join(entetes) + "\n"
    f.write(ligneEntete)
    for i in multiForecast_city:
        for x in i.list:
            f.write(i.city.name)
            f.write(";")
            f.write(str(round(x.main.temp)) + "°c")
            f.write(";")
            f.write(str(round(x.main.tempmin)) + "°c")
            f.write(";")
            f.write(str(round(x.main.tempmax)) + "°c")
            f.write(";")
            f.write(str(x.dttxt))
            f.write(";")
            f.write("\n")
    f.close()
    print("Copie CSV Fini")
