with open("input.txt", "r", encoding="utf-8") as fichier_entree:
    contenu = fichier_entree.read
mots = contenu.split()
nombre_mots = len(mots)
contenu_maj = contenu.upper()
with open("output.txt", "w", encoding="utf-8") as fichier_sortie:
    fichier_sortie.write("=== TEXTE EN MAJUSCULES ===\n\n")
    fichier_sortie.write(contenu_maj + "\n\n")
    fichier_sortie.write(f"Nombre total de mots : {nombre_mots}\n")

print("✅ Le fichier 'output.txt' a été créé avec succès !")
