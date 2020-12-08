import pandas as pd

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

#Pointure la moins vendu
tailleMoinsVendu = count_size.tail(10)

#Les états qui achète le plus
count_buyer = buyer_region.value_counts()
etats_max = count_buyer.head(10)

#Les états qui achète le moins
etats_min = count_buyer.tail(10)

#La marque qui achéte le plus
count_brand = brand.value_counts()
marque_max = count_brand.head(1)

#La marque qui achète le moins
marque_min = count_brand.tail(1)

#Les modèles les plus vendus
count_sneaker = sneaker_name.value_counts()
modele_max = count_sneaker.head(10)

#Les modèles les moins vendus
modele_min = count_sneaker.tail(10)

#Nombre de vente total
vente_total = len(sale_price)