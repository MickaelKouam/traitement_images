""" Exercice image 
Créer le programme qui garde l’image d’origine en modifiant tous les pixels vert
en blanc puis sauvegarde l'image resultante.
"""

from PIL import Image, ImageDraw
img = Image.open("/home/kouamen/Images/recadrage_gimp.png")
print(img.size)
largeur_image, hauteur_image= img.size
print("largeur_image = ",largeur_image, "hauteur_image = ", hauteur_image)
for y in range(hauteur_image):
	for x in range(largeur_image):
		rouge,vert,bleu=img.getpixel((x,y))

		# test sur la valeur d'un pixel precis
		# if y == 450 and x == 121:
		# 	rouge,vert,bleu=img.getpixel((x,y))
		# 	print(rouge, vert, bleu)  # test pour afficher les coordonne couleur d'un pixel precis

		## attribution de la couleur blanche au pixel modifier pour test
		# 	nouveau_rouge=255
		# 	nouveau_vert=255
		# 	nouveau_bleu=255
		## modification des pixels avec les nouvelle valeurs
		# 	img.putpixel((x,y),(nouveau_rouge,nouveau_vert,nouveau_bleu))
		# # fin test valeur d'un pixel

		# verification du parcours correct de l'image entiere
		# print ("Rouge = ", rouge, "Vert = ", vert, "Bleu = ", bleu)

		# condition pour modifier lesw pixel vers sur mon image
		if rouge > 150 and rouge < 190 and vert > 168 and vert < 195 and bleu > 118 and bleu < 180:
			nouveau_rouge=190
			nouveau_vert=189
			nouveau_bleu=184
			img.putpixel((x,y),(nouveau_rouge,nouveau_vert,nouveau_bleu))

img.show()
img.save("FondVertSuppr.jpg")