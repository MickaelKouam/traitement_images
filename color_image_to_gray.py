""" Exercice image 
Créer le programme qui garde l’image d’origine au-dessus d’une diagonale
et qui transforme en niveaux de gris en-dessous de celle-ci.
"""

from PIL import Image
img = Image.open("recadrage_gimp.png")  # donner le chemin correct

largeur_image, hauteur_image= img.size
print("largeur_image = ",largeur_image, "hauteur_image = ", hauteur_image)
for y in range(hauteur_image):
	for x in range(y):
		if x > largeur_image:
			continue
		elif x < largeur_image:			
			#print("Y = ",y, "X = ",x)
			rouge,vert,bleu=img.getpixel((x,y))  # access aux valeurs des pixels
			nouveau_rouge=(vert+bleu+rouge)//3
			nouveau_vert=(vert+bleu+rouge)//3
			nouveau_bleu=(vert+bleu+rouge)//3
			img.putpixel((x,y),(nouveau_rouge,nouveau_vert,nouveau_bleu))

img.show()
img.save("diagonaleGrise3.jpg")