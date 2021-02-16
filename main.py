import modules.api.api as api
import modules.csv.csv as csv
import modules.myVar as Var

firstCity = input("Entrez la ville ")

coord = api.currentCoord(firstCity, Var.api_key)
multiCity = api.circle(coord[0], coord[1], Var.api_key, Var.cnt)

for i in multiCity:
    api.forecast(i, Var.api_key)
csv.copie(Var.tabCity)

csv.recherche(firstCity)
