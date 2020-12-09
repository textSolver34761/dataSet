import pandas as pd
import json
from json.decoder import JSONDecodeError

def datajson(value):
    result = value.to_json(orient="index")
    parsed = json.loads(result)
    return json.dumps(parsed, indent=4)
 
#Ouverture du fichier de donnés
data = pd.read_csv('C:\stockx.csv')

#Définition des colonnes
order_date = data['Order Date']
brand = data['Brand']
sneaker_name = data['Sneaker Name']
sale_price = data['Sale Price']
retail_price = data['Retail Price']
release_date = data['Release Date']
shoe_size = data['Shoe Size']
buyer_region = data['Buyer Region']

#Prix moyen de vente
sale_price_int = sale_price.str[1:]
sale_price_point = sale_price_int.str.replace(',','')
sale_price_final = sale_price_point.astype(int)
prixMoyenVente = round(sale_price_final.mean(), 2)

#Prix de vente le plus élevé
prixEleverVente = sale_price_final.max()

#Prix de vente le plus bas
prixBasVente = sale_price_final.min()

#Pointure moyenne 
tailleMoyenne = round(shoe_size.mean(), 2)

#Pointure la plus élevé
tailleEleve = shoe_size.max()

#Pointure la plus basse
tailleBasse = shoe_size.min()

#Pointure la plus vendu
count_size = shoe_size.value_counts()
taillePlusVendu = count_size.head(10)
taillePlusVenduJson = datajson(taillePlusVendu)

#Pointure la moins vendu
tailleMoinsVendu = count_size.tail(10)
tailleMoinsVenduJson = datajson(tailleMoinsVendu)

#Les états qui achète le plus
count_buyer = buyer_region.value_counts()
etats_max = count_buyer.head(10)
etats_maxJson = datajson(etats_max)

#Les états qui achète le moins
etats_min = count_buyer.tail(10)
etats_minJson = datajson(etats_min)

#La marque qui achéte le plus
count_brand = brand.value_counts()
marque_max = count_brand.head(1)

#La marque qui achète le moins
marque_min = count_brand.tail(1)

#Les modèles les plus vendus
count_sneaker = sneaker_name.value_counts()
modele_max = count_sneaker.head(10)
modele_maxJson = datajson(modele_max)

#Les modèles les moins vendus
modele_min = count_sneaker.tail(10)
modele_minJson = datajson(modele_min)

#Nombre de vente total
vente_total = len(sale_price)

#Les dix dernières ventes
dix_dernière_vente = data.tail(10)
dix_dernière_venteJson = datajson(dix_dernière_vente)

#Ecriture dans un fichier json
dictionnaire = {}
dictionnaire["prixMoyenVente"] = prixMoyenVente
dictionnaire["prixEleverVente"] = float(prixEleverVente)
dictionnaire['prixBasVente'] = float(prixBasVente)
dictionnaire['tailleMoyenne'] = tailleMoyenne
dictionnaire['tailleEleve'] = tailleEleve
dictionnaire['tailleBasse'] = tailleBasse
dictionnaire['taillePlusVenduJson'] = taillePlusVenduJson
dictionnaire['tailleMoinsVenduJson'] = tailleMoinsVenduJson
dictionnaire['etatsMaxJson'] = etats_maxJson
dictionnaire['etatsMinJson'] = etats_minJson
dictionnaire['marqueMax'] = int(marque_max)
dictionnaire['marqueMin'] = int(marque_min)
dictionnaire['modeleMaxJson'] = modele_maxJson
dictionnaire['modeleMinJson'] = modele_minJson
dictionnaire['venteTotal'] = vente_total
dictionnaire['dixDerniereVenteJson'] = dix_dernière_venteJson

with open('data.json', 'w') as fp:
    json.dump(dictionnaire, fp)