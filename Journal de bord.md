# Objectif 
____________________

_Créer un petit jeu inspiré de Space Invaders, revisité avec l’univers graphique et sonore de Pac-Man. 
Le joueur est Pac-Man, qui se déplace horizontalement et tire pour toucher (4) fantômes ennemis.
Les ennemis ne meurent pas mais augmentent le score quand ils sont touchés. Ils peuvent aussi tirer. Le joueur doit éviter leurs tirs.
Des obstacles se situent entre Pac-Man et les fantômes afin de se protéger des tirs.
Le jeu s’intensifie progressivement : la vitesse des ennemis et la fréquence des tirs augmentent, jusqu’à un palier.
Un bonus spécial circulera en haut de l’écran : s’il est atteint par un tir, Pac-Man obtient un multiplicateur de score temporaire (*n).
Le score s’affiche, un son est joué pour chaque tir et chaque collision. Un bouton permet de rejouer à la fin. Un mode d'emploi 
avec les commandes sera affiché au début et le but du jeu avec éventuellement les précédents meilleurs scores._

# Journal de bord
_________________

#### 26 Juin :

* 1er RDV avec le mentor
* Familiarisation avec l’éditeur de code _Pycharm_
* 1ère idée de projet : Un Space Invaders dans l’univers Pac-Man et les décors asssociés, avec à la place des ennemis,
des fantômes et pour le joueur, Pac man.

#### 27 Juin :

* 1er dépôt après réinitialisation du code de test
* Installation de la bibliothèque _Pygame_
* Incorporation d’un code d’exemple _Pycharm_, d'un cercle qui bouge

#### 28 Juin :

* Ajout du journal de bord sur Github
* Renvoi du projet au mentor

#### 29 Juin :

* Modification du déplacement du joueur
* Adaptation de l'écran en format de jeu rétro

#### 30 Juin :

* Limitation du mouvement du joueur sur l'axe x : Difficultés à comprendre l’usage de min() et max() 
pour limiter le déplacement du joueur, notamment pourquoi il fallait inclure `player_pos.x` dans la comparaison.
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

#### 01 Juillet :

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

#### 02 Juillet :

* Insertion d'un premier croquis de jeu

#### 04 Juillet :

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

#### 06-09 Juillet :

* Déplacement des 4 ennemis en boucle : J’ai enfin réussi à faire fonctionner le déplacement en boucle des ennemis. 
Pour cela, j’ai d’abord défini les positions précises des quatre coins du rectangle noir 
qui délimite la surface de déplacement des fantômes. J’ai commencé par faire tous les tests avec un seul fantôme 
pour observer le comportement plus facilement, puis j’ai copié le même fonctionnement pour les autres. Le déplacement 
se fait désormais en boucle dans le sens horaire, en passant par les quatre coins du rectangle. Je prévois d’optimiser 
le code plus tard pour qu’il soit plus compact, car il est actuellement quatre fois trop long et peu pratique 
à modifier si je veux ajouter un nouveau fantôme. Le problème qui m’a bloqué venait d’une coordonnée incorrecte 
assignée à un des coins du rectangle, ce que je n’ai remarqué qu’au bout de trois jours.

#### 09 Juillet : 

* Collisions avec les ennemis et le tir : J'ai crée des intervalles en x et y délimitant le rectangle formant les ennemis 
en fonction de si le tir passe à travers cette intervalle et s'il y passe il retourne à la position du joueur.

#### 10 Juillet :

* Implémentation du système de score : J'ai réussi à afficher le score à l'écran, mais j'ai eu du mal à comprendre les 
f-strings pour formater le texte. J'ai appris qu'elles permettent d'insérer des valeurs de variables directement dans une 
chaîne de caractères avec des informations dynamiques qui changent. J'ai également découvert que le 
`True` dans `font.render(f"SCORE: {score}", True, ("color"))` est un booléen qui active _l'anti-aliasing_, 
de ce que j'ai compris ça rend le texte plus lisible.

#### 11 Juillet : 

* Ajout d'un document de bibliographie
* Regroupements en liste des commandes de collisions et déplacement en boucles des ennemis : Quelques difficultés
avec la syntaxe des deux listes que j'ai dû utiliser pour le déplacement en boucles
* Changement de quelques noms pour améliorer la cohérence

#### 12 Juillet :

* Système automatique de tir ennemi, encore en cours : 
Le but est de pouvoir utiliser les dimensions du tir joueur pour les donner aux tirs ennemis. 
J'ai eu comme problèmes le retour à la position du joueur car je compte garder pour le moment le cercle 
(vu que Pac-Man est ± rond) et j'ai dû réajuster la commande de copie:
```
bullet_player_pos = player_pos.copy() 
```
En cette version pour ajuster les dimensions du rectangle :
```
bullet_player_pos.x = player_pos.x - 5
bullet_player_pos.y = player_pos.y - 5
```
Un autre problème est survenu : le déplacement. Les tirs n'avançaient pas à la même vitesse ni au même endroit que leur 
ennemi respectif. Cela m'a pris un peu de temps à comprendre après plusieurs tests, malgré le code juste, le problème
résidait dans une erreur d'imbrication:
```
for i in range(0, len(ghosts_pos)):         # Parmi la liste de positions et de directions des fantômes
     pos = ghosts_pos[i]
     direction = ghosts_direction[i]
     ...
     for i in range(0, len(bullet_ghosts_pos)):          # Parmi la liste de positions et de directions des tirs fantômes
         pos = bullet_ghosts_pos[i]
         direction = bullet_ghosts_direction[i]
         ...
```
Au lieu de :
```
for i in range(0, len(ghosts_pos)):         # Parmi la liste de positions et de directions des fantômes
     pos = ghosts_pos[i]
     direction = ghosts_direction[i]
     ...
for i in range(0, len(bullet_ghosts_pos)):          # Parmi la liste de positions et de directions des tirs fantômes
     pos = bullet_ghosts_pos[i]
     direction = bullet_ghosts_direction[i]
     ...
```
Maintenant mon dernier problème est que je commence à ne plus m'y retrouver dans le code. Je pense maintenant à faire 
des classes d'objets car je n'ai pas réussi à trouver le souci de mon tir ennemi qui ne suivait plus la direction que je
voulais en descendant vers le joueur. Je n'ai donc pas encore la solution pour faire le tir ennemi mais je vais plutôt 
me pencher maintenant sur une refonte quasi total du code.


# Planification
_______________

#### Semaine du 30.06 - 06.07 :

* Conception des bordures de l'écran ~ FAIT
* Conception du joueur se déplaçant de gauche à droite  FAIT
* Conception de Pac Man qui tire  FAIT
* Conception du retour du tir après être sorti de l'écran pour pouvoir tirer plusieurs fois  FAIT
* Créer et afficher les 4 fantômes ennemis  FAIT
* Faire un déplacement en boucle de ces ennemis FAIT

#### Semaine du 07.07 - 13.07 :

* Ajouter les collisions entre tir et fantôme FAIT
* Faire augmenter le score quand un fantôme est touché et l'afficher FAIT
* Regrouper sous formes de listes ou de tableaux FAIT
* Faire tirer les ennemis et faire perdre le joueur

#### Semaine du 14.07 - 20.07 :

* Créer un bonus qui se déplace dans un mini-circuit en haut de l’écran
* Gérer la collision entre Pac-Man et le bonus
* Ajouter le tir du joueur avec nouvelle limite (2 tirs par seconde)
* 

#### Semaine du 21.07 - 27.07 :

*  
