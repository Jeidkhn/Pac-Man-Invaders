# Objectif 
____________________

_Créer un petit jeu inspiré de Space Invaders, revisité avec l’univers graphique et sonore de Pac-Man. 
Le joueur est Pac-Man, qui se déplace horizontalement et tire pour toucher (4) fantômes ennemis.
Les ennemis ne meurent pas, mais augmentent le score quand ils sont touchés. Ils peuvent aussi tirer. Le joueur doit éviter leurs tirs.
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
Notamment la différence entre ces lignes (faux) : 
```
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_pos = player_pos
```
Et ces lignes (juste) :
```
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
bullet_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.1)
```
J'ai donc compris que dans ce cas le joueur et le tir sont différents, car il y a maintenant deux objets.
* Ajout de commentaires pour mieux me retrouver dans le code au fur et à mesure que j'avance dans le projet
* Limitation du mouvement du tir sur l'axe x, car après test, il partait 
exactement comme le joueur sans ses limites de déplacement

#### 01 juillet :

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

#### 02 juillet :

* Insertion d'un premier croquis de jeu

#### 04 juillet :

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
Dans le cas du cercle la répartition des pixels se fait au milieu de la forme c.-à-d. qu'autant de pixels 
se trouvent en -x, -y qu'en +x, +y par rapport au point de position. Concernant la position donnée, je l'ai détérminé
en calculant le perimètre de la surface sur laquelle se trouvent les fantômes en veillant à prendre la largeur/hauteur 
des ennemis en compte. Afin qu'ils soient inscrits dans la surface rectangulaire.

#### 06-09 juillet :

* Déplacement des 4 ennemis en boucle : j'ai enfin réussi à faire fonctionner le déplacement en boucle des ennemis. 
Pour cela, j’ai d’abord défini les positions précises des quatre coins du rectangle noir 
qui délimite la surface de déplacement des fantômes. J’ai commencé par faire tous les tests avec un seul fantôme 
pour observer le comportement plus facilement, puis j’ai copié le même fonctionnement pour les autres. Le déplacement 
se fait désormais en boucle dans le sens horaire, en passant par les quatre coins du rectangle. Je prévois d’optimiser 
le code plus tard pour qu’il soit plus compact, car il est actuellement quatre fois trop long et peu pratique 
à modifier si je veux ajouter un nouveau fantôme. Le problème qui m’a bloqué venait d’une coordonnée incorrecte 
assignée à un des coins du rectangle, ce que je n’ai remarqué qu’au bout de trois jours.

#### 09 juillet : 

* Collisions avec les ennemis et le tir : j'ai crée des intervalles en x et y délimitant le rectangle formant les ennemis 
en fonction de si le tir passe à travers cette intervalle et s'il y passe il retourne à la position du joueur.

#### 10 juillet :

* Implémentation du système de score : J'ai réussi à afficher le score à l'écran, mais j'ai eu du mal à comprendre les 
f-strings pour formater le texte. J'ai appris qu'elles permettent d'insérer des valeurs de variables directement dans une 
chaîne de caractères avec des informations dynamiques qui changent. J'ai également découvert que le 
`True` dans `font.render(f"SCORE: {score}", True, ("color"))` est un booléen qui active _l'anti-aliasing_, 
de ce que j'ai compris ça rend le texte plus lisible.

#### 11 juillet : 

* Ajout d'un document de bibliographie
* Regroupements en liste des commandes de collisions et déplacement en boucles des ennemis : Quelques difficultés
avec la syntaxe des deux listes que j'ai dû utiliser pour le déplacement en boucles
* Changement de quelques noms pour améliorer la cohérence

#### 12 juillet :

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

#### 05 août - 03 septembre :

* Nettoyage et réorganisation du code pour le rendre plus clair. Regroupement des variables et fonctions par thème : joueur, ennemis, tirs.
* Réflexion sur l’utilisation de classes pour simplifier les déplacements et collisions pour la suite (je dois encore les ajouter)
* Suppression en cours du code redondant et simplification des boucles pour les ennemis.
* Ajout de commentaires à revoir pour mieux comprendre le fonctionnement du jeu.

#### 5 septembre : 

* 2ème RDV Mentor, prise de conscience de la direction dans laquelle je vais répondre aux questions:
1) Problématique : Pac-Man se déplace uniquement à l’horizontale et peut tirer (limité à 2 tirs/s).
Les ennemis (4 fantômes) tournent en boucle et tirent aussi.
Le joueur marque des points en touchant les fantômes, mais ils ne meurent pas.
Le joueur perd s’il est touché par un tir ennemi.
Il existe un bonus qui donne un multiplicateur de score temporaire (*5).
Le jeu s’intensifie progressivement (vitesse ennemis + fréquence de tirs ennemis).
2) Ressources : Quelques vidéos ont été vues, des forums et l'aide de mon père pour l'approche
à avoir notamment d'orientation objet, qui m'a donc conduit à recommencer en partie.
3) Calendrier : Encore à voir


#### 9 septembre : 

* Ajout des tirs ennemis.

#### 11 septembre :

* Ajout du score en classe et encore du nettoyage.

#### 12 septembre : 

* 

#### 13 septembre : 

* Refonte du code en programmation orientée objet (POO) quaisment terminé : J'ai mis à jour quasiment tout sauf 
encore les collisions joueur - tirs fantômes et fantômes - tir joueur, et la gestion des tirs hors écran. 
J'arriverai donc au même niveau que l'avant POO après ces étapes.
* Changements de constantes en variables

#### 14 septembre : 

* Ajout de collisions des tirs sur fantômes et sur joueur (non-orienté objet)
* Ajout de points au Score après cible atteinte
* Suppression des tirs hors écran 

#### 22 octobre :

* Ajout de la classe CollisionManager afin de gérer les collisions entre objet

#### 24 octobre :

* Classe utilitaire : De ce que j'ai compris c'est une classe qui permet d'avoir la structure toujours 
sous formes de classe mais sans l'identité objet au début et se contente d'avoir "l'armature" :
Classe avec identité :

```
    class Player:
    def __init__(self, x, y, color, width, screen, speed, bullet_Manager):
        self.position = pygame.Vector2(x, y)
        self.width = width
        self.color = color
        self.screen = screen
        self.speed_move = speed
        self.bullet_Manager = bullet_Manager
```
Classe utilitaire : 
```
    class CollisionManager:
    pass
```
J'étais bloqué car je cherchais comment appliquer la méthode sans objets et là je suis débloqué.

#### 30 Octobre : 

* Ajout collision tir joueur - fantômes et tir fantômes - joueur

#### 31 octobre :

* Modification tir supprimé après collisions

#### 2 novembre : 

* Correction en cours du tir joueur sur les fantômes et le tir hors de l'écran.

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

#### Semaine du 08.09 - 14.09 :

* Rajouter les collisions entre tir et fantôme
* Réafficher le score FAIT
* Ajouter le tir du joueur avec nouvelle limite (2 tirs par seconde)
* Faire tirer les ennemis FAIT
* Faire perdre le joueur 
* Créer un bonus qui se déplace dans un mini-circuit en haut de l’écran
* Gérer la collision entre Pac-Man et le bonus

#### Semaine du 15.09 - 21.09 :

* Rajouter les collisions entre tir et fantôme ~FAIT
* Faire perdre le joueur et collisions tir ennemi sur joueur ~FAIT
* Faire augmenter le score ~FAIT
* Ajouter le tir du joueur avec nouvelle limite (2 tirs par seconde)
* Créer un bonus qui se déplace dans un mini-circuit en haut de l’écran
* Gérer la collision entre Pac-Man et le bonus

#### Semaine du 03.11 - 09.11 :

* Corriger la collision du tir joueur sur fantôme
* Ajouter le tir du joueur avec nouvelle limite (2 tirs par seconde)
* Créer un bonus qui se déplace dans un mini-circuit en haut de l’écran
* Gérer la collision entre Pac-Man et le bonus


