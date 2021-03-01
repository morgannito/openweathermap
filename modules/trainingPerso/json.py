# Permet d'enregistrer dans un fichier json
# @param tab: json
def copieJson(tab):
    fichier = open("json.json", "wb")
    fichier.write(tab)
    fichier.close()
    print("Copie Json Terminée")