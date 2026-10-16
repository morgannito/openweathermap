# Permet d'enregistrer dans un fichier json
# @param tab: json
def copieJson(tab):
    with open("json.json", "wb") as fichier:
        fichier.write(tab)
    print("Copie Json Terminée")