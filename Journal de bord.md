# Objectif 
____________________

_Créer un petit jeu inspiré de Space Invaders, revisité avec l’univers graphique et sonore de Pac-Man. 
Le joueur est Pac-Man, qui se déplace horizontalement et tire pour toucher (4) fantômes ennemis.
Les ennemis ne meurent pas mais augmentent le score quand ils sont touchés. Ils peuvent aussi tirer. Le joueur doit éviter leurs tirs.
Des obstacles se situent entre Pac-Man et les fantômes afin de se protéger des tirs.
Le jeu s’intensifie progressivement : la vitesse des ennemis et la fréquence des tirs augmentent, jusqu’à un palier.
Un bonus spécial circulera en haut de l’écran : s’il est atteint par un tir, Pac-Man obtient un multiplicateur de score temporaire (*n).
Le score s’affiche, un son est joué pour chaque tir et chaque collision. Un bouton permet de rejouer à la fin. Un mode emploi avec les commandes sera affiché au début et le but du jeu avec 
éventuellement les précédents meilleurs scores._

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
Et ces lignes (juste):
```
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
```
J'ai donc compris que dans ce cas le joueur et le tir sont différents, car il y a maintenant 2 objets.
* Ajout de commentaires pour mieux me retrouver dans le code au fur et à mesure que j'avance dans le projet
* Limitation du mouvement du tir sur l'axe x, car après test il partait 
exactement comme le joueur sans ses limites de déplacement

#### 01 Juillet 2025 :

* Retour du tir au joueur après dépassement de l'écran : La convention dans les languages informatiques 
du sens de l'axe y en comparaison avec les maths me fait encore un peu défaut quand je dois me représenter 
les valeurs.
Notamment dans mon cas :
```
if bullet_pos.y <= 0:   
```
Et non :
```
if bullet_pos.y <= 720:   
```

#### 02 Juillet 2025 :

* Insertion d'un premier croquis de jeu

#### 04 Juillet 2025 :

* Ajout de l'objectif écrit de mon projet pour pouvoir mieux m'orienter dans la planification
* Changement de la façon d'exprimer la position pour le joueur, le tir et les ennemis, pour avoir plus de cohérence
par la suite. Étant donné que la taille de l'écran devrait rester dans ce format rétro et que cela reste plus simple 
pour moi à visualiser. Donc au lieu d'exprimer ma position avec :
```
..._pos = pygame.Vector2(screen.get_width(), screen.get_height())
```
Je vais plus souvent la définir ainsi :
```
..._pos = pygame.Vector2(x,y)
```
* Ajout des 4 ennemis sans déplacement, ni tir : Après constation d'un changement au niveau de la répartition des pixels
de largeur/hauteur en fonction de `pygame.draw.rect` et `pygame.draw.circle`. J'ai fait plusieurs tests et j'ai compris que pour
un rectangle, les pixels vont commencer à partir du point défini de position sur l'écran et continuer en +x et +y (sens conventionnel informatique).
Dans le cas du cercle la répartition des pixels se fait au milieu de la forme c-à-d qu'autant de pixels 
se trouvent en -x/y qu'en +x/y par rapport au point de position. Concernant la position donnée, je l'ai détérminé
en calculant le perimètre de la surface où se trouve les fantômes en veillant à prendre la largeur/hauteur 
des ennemis en compte. Afin qu'ils soient inscrits dans le surface rectangulaire.

#### 05 Juillet 2025 :

* 

# Planification
_______________

#### Semaine du 30.06 - 06.07 :

* Conception des bordures de l'écran ~ FAIT
* Conception du joueur se déplaçant de gauche à droite  FAIT
* Conception de Pac Man qui tire  FAIT
* Conception du retour du tir après être sorti de l'écran pour pouvoir tirer plusieurs fois  FAIT
* Créer et afficher les 4 fantômes ennemis  FAIT
* Faire un déplacement en boucle de ces ennemis

#### Semaine du 07.07 - 13.07 :

* Ajouter le tir du joueur avec nouvelle limite (2 tirs par seconde)
* Ajouter les collisions entre tir et fantôme
* Faire augmenter le score quand un fantôme est touché
* Afficher le score à l’écran
* Créer un bonus qui se déplace dans un mini-circuit en haut de l’écran
* Gérer la collision entre Pac-Man et le bonus

#### Semaine du 14.07 - 20.07 :

*

#### Semaine du 21.07 - 27.07 :

*  
