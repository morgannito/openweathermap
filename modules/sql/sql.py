#!/usr/bin/env python
# -*- coding: utf-8 -*
import configparser  # Permet de parser le fichier de paramètres

config = configparser.RawConfigParser()  # On créé un nouvel objet "config"
config.read('config.ini')  # On lit le fichier de paramètres

# On récupère les valeurs des différents paramètres ATTENTION, cette syntaxe est spécifique pour les paramètres MySQL
# On créé un dictionnaire contenant les paires clés/valeurs Pour chaque paramètre, on utilise la fonction "get" de
# notre objet "config" en lui indiquant la section et le nom du paramètre
paramMysql = {
    'host': config.get('MYSQL', 'host'),
    'user': config.get('MYSQL', 'user'),
    'passwd': config.get('MYSQL', 'pass'),
    'db': config.get('MYSQL', 'db')
}
