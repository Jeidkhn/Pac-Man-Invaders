# python
import os
import pygame

def charger_image(nom_fichier: str) -> pygame.Surface:

    dossier_images = os.path.join(os.path.dirname(__file__), "images")
    chemin = os.path.join(dossier_images, nom_fichier)

    image = pygame.image.load(chemin)

    if image.get_alpha() is not None:
        image = image.convert_alpha()
    else:
        image = image.convert()

    return image
