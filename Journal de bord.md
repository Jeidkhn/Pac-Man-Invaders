# Journal de bord
_________________

#### 26 Juin 2025 :

* 1er RDV avec le mentor
* Familiarisation avec l’éditeur de code _Pycharm_
* 1ère idée de projet : Un Space Invaders dans l’univers Pac-Man et les décors asssociés, avec à la place des ennemis,
des fantômes et pour le joueur, Pac man.

#### 27 Juin 2025 :

* 1er dépôt après réinitialisation du code de test
* Installation de la bibliothèque _Pygame_
* Incorporation d’un code d’exemple _Pygame_, d'un cercle qui bouge

#### 28 Juin 2025 :

* Ajout du journal de bord sur Github
* Renvoi du projet au mentor

#### 29 Juin 2025 :

* Modification du déplacement du joueur
* Adaptation de l'écran en format de jeu rétro

#### 30 Juin 2025 :

* Limitation du mouvement du joueur sur l'axe x : Difficultés à comprendre l’usage de min() et max() 
pour limiter le déplacement du joueur, notamment pourquoi il fallait inclure _player_pos.x_ dans la comparaison.
* Tir du joueur : Difficultés à comprendre pourquoi les deux éléments du jeu bougent en même temps, donc comprendre 
la différence entre la copie d'un scalaire et la référence d'un objet. 
Notamment la différence entre ces lignes (faux): 
```
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_pos = player_pos
```
et ces lignes (juste):
```
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
```
J'ai donc compris que dans ce cas le joueur et le tir sont différents, car il y a maintenant 2 objets.
* Ajout de commentaires pour mieux me retrouver dans le code au fur et à mesure que j'avance dans le projet
* Limitation du mouvement du tir sur l'axe x, car après test il partait 
exactement comme le joueur sans ses limites de déplacement

#### 01 Juillet 2025 :

*


# Planification
_______________

#### Semaine du 30.06 - 06.07 :

* Conception des bordures de l'écran
* Conception du joueur se déplacant de gauche à droite
* Conception de Pac Man qui tire
* Conception du retour du tir après être sorti de l'écran pour pouvoir tirer plusieurs fois 
* Conception d'un premier ennemi

#### Semaine du 07.07 - 13.07 :

*
