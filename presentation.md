# Présentation du projet LabyMaze

## Présentation globale
##### Nous sommes passionnés de jeux vidéo et ce depuis notre enfance, c'est pourquoi notre idée principale est de créer un jeu qui mêle difficulté et montée en niveau ce qui constitue notre problématique. Notre objectif est de créer un jeu qui puisse faire passer le temps de manière amusante sans trop de difficulté et sans qu'il soit trop long afin de ne pas ennuyer le joueur.

## Présentation de l'équipe
##### Notre équipe est composée de Jules Bonneau, Souhail El Kadi , Emilien Pradal et David Lovis.
* ##### Jules Bonneau s'occupe de créer les zones de jeu, c'est à dire les labyrinthes. Il s'occupe de la collision entre le joueur et les murs, de la génération d'une zone à une autre, ainsi que du changement de menus.
* ##### Souhail El Kadi s'occupe de la génération de la lave, des paramètres du joueur, ainsi que du développement du jeu de chance.
* ##### Emilien Pradal s'occupe du fonctionnement de la monnaie du jeu, à savoir les pièces, du programme de la création de murs, ainsi que du retour au menu lorsque le joueur meurt.
* #### David Lovis s'occupe du graphisme, c'est-à-dire des illustrations qui apparaissent dans le jeu. Il s'occupe aussi de la configuration du menu.
#### Le temps que nous avons passé sur ce projet est d'environ 20 heures.

## Les étapes de notre projet
* ### Etape 1 : Recherche du projet
#### Au départ, nous voulions créer un jeu de style RPG (Role Playing Game) en 3 dimensions avec une histoire et des armes avec lesquelles combattre des ennemis. Plus tard nous avons abandonné cette idée car elle aurait pris trop de temps à être réalisée et était trop complexe pour notre niveau. Ainsi nous avons réfléchi à une autre option celle de l'escape game. Nous voulions créer de la fausse trois dimensions (De la deux dimensions mais avec un effet de profondeur qui fait croire au joueur qu'il est en trois dimensions) mais cette idée fut très vite abandonnée car elle ne plaisait pas à tous les membres du groupe. Finalement nous avons opté pour un jeu en deux dimensions de type labyrinthe où le joueur doit parcourir plusieurs labyrinthes tout en étant poursuivi par de la lave. Auquel nous avons ajouté un jeu de chance et de hasard car nous aimons les paris risqués.

* ### Etape 2 : Debut de la réalisation du projet
#### Nous avons d'abord démarré par créer un cube pouvant se déplacer dans toutes les directions. Notre premier problème a été de créer des murs avec lesquels nous ne pouvions pas passer à travers. Après beaucoup de réflexion nous avons réussi à résoudre ce problème en faisant en sorte d'associer ces rectangles à des coordonnées que le joueur ne peut pas traverser.
* ### Etape 3 : Avancement de chacun dans le projet
#### A ce moment-là notre priorité était de mener à bien la création de nos labyrinthes afin qu'il n'y ait pas de problèmes ou de bugs. Jules Bonneau avait commencé à créer les zones de jeu (les labyrinthes) à l'aide de notre programmes avec les rectangles et les coordonnées (voir étape 2), Souhail El Kadi commençait à créer son système de lave qui monte petit à petit, Emilien Pradal préparait le système de mort du joueur, tandis que David Lovis illustrait certains éléments du jeu, notamment les boutons du menu.

* ### Etape 4 : Mise en commun du travail de chacun
#### A ce stade-là, nous avons réuni tous nos travaux et les avons reliés via le menu que nous venions de créer. Le problème qui s'est posé était que nous n'arrivions pas à implémenter le jeu de labyrinthe dans le menu. De ce fait, après réfléxion et ajustements, nous avons réussi à relier les deux programmes. Emilien Pradal préparait le système de pièces qui serait crucial pour le jeu de chance et de hasard que nous voulions créer.

* ### Etape 5 : Fin du projet
#### La dernière étape de notre projet était de créer et d'implémenter notre jeu de chance et de hasard. Après beaucoup de travail, nous avons réussi à l'implémenter et à faire en sorte qu'il soit actif dans le jeu de labyrinthe. C'est ainsi que nous avons terminé notre projet.

## Vérification de l'opérationnalité et du fonctionnement du projet

#### Au moment du dépôt, nous avons fini le jeu que nous voulions réaliser. Afin de vérifier l'absence de potentiels bugs dans notre jeu, nous avons relancé le jeu plusieurs fois avec une vitesse différente pour le joueur à chaque essai. Ainsi nous avons trouvé deux problèmes, le premier est que lorsque l'on dirige notre joueur avec les touches traditionnellement utilisées dans le monde des jeux vidéo : ZQSD, le joueur pouvait se retrouver bloqué, collé à un mur, alors que lorsque l'on utilise les flèches directionnelles du clavier, aucun problème ne survenait. Nous avons donc supprimé l'usage des touches ZQSD. Le deuxième problème est que lorsque le joueur possède une vitesse supérieure à la vitesse normale, il ne peut pas se coller directement aux murs, il existe un espace vide entre le mur et le joueur. Nous n'avons pas réussi à régler ce problème, cependant il n'empêche en aucun cas le bon déroulement du jeu. Afin de vérifier s'il y avait d'autres bugs, nous avons décidé de réfléchir et de regrouper tous les bugs qui auraient pu survenir dans notre jeu, puis les tester pour voir s'ils fonctionnaient. Aucun d'eux ne fonctionnait ce qui signifie que le jeu est bien programmé.

## Bilan

#### Jules Bonneau : J'ai énormément apprécié préparer ce projet et travailler dessus, cela m'a permis de me concentrer sur un objectif et de travailler en équipe afin d'y parvenir. Je pense que le projet aurait tout de même pu être légèrement amélioré. En effet le réglage du problème de l'espace vide entre un mur et un joueur lorsque la vitesse du joueur augmente aurait pu être réglé. Le décor du menu de packs aurait pu être mieux travaillé et être attractif. De plus je pense que l'ajout d'une musique aurait pu être bénéfique pour l'expérience de jeu. Je trouve le jeu amusant et attractif même si, petit à petit, il peut être légèrement ennuyeux. L'aspect en deux dimensions rappelle les jeux rétro que j'apprécie particulièrement. Grâce à ce projet j'ai pu développer mes compétences en programmation et mon travail en équipe.

#### David Lovis : Lors de ces séances passées avec mes camarades, je fus plutôt satisfait de mon travail envers l’équipe. En effet j’ai dirigé au départ les idées et les répartitions de tâches puis nous avons chacun avancé à notre rythme vers nos objectifs. Je me suis occupé en majorité de l’interface graphique et du menu du jeu, accompagné du logo. Nous avions rencontré de temps en temps des difficultés au fil des cours passés mais nous n’avons jamais lâché prise, y compris moi. J’ai pu grâce à ce projet développer des compétences en programmation, notamment en « POO », qui m’était très difficile de maîtriser au départ. Cependant grâce au temps passé sur ce projet, j’ai pu améliorer ces compétences et combler certaines de mes lacunes. Mes idées pour améliorer ce projet furent d’implémenter un système de « packs ». Ce système permet donc d’augmenter la difficulté du jeu et de créer une sorte de progression dans le jeu pour atteindre la fin des 3 niveaux.

#### Souhail El Kadi : Pendant ce projet réalisé avec mon groupe, j’ai trouvé le travail intéressant et motivant. Il y avait une bonne cohésion entre nous, ce qui nous a permis d’avancer ensemble de manière sérieuse et efficace. Chacun a participé au projet, partageait ses idées et faisait de son mieux pour faire avancer le jeu. De mon côté, j’ai contribué à plusieurs éléments importants du projet. J’ai notamment mis en place le cadre du labyrinthe, la lave ainsi que le système de pièces. Certaines parties n’ont pas toujours été simples à réaliser, mais cela m’a permis de chercher des solutions et de mieux comprendre certains aspects du développement. Ce projet m’a beaucoup aidé à renforcer mes compétences en programmation. J’ai pu progresser sur plusieurs notions et devenir plus à l’aise dans ma manière de coder. Par exemple, la POO me semblait plus difficile au début, mais grâce au travail réalisé sur ce projet, je la comprends maintenant mieux et je suis plus confiant dans son utilisation. 

#### Emilien Pradal : J’ai trouvé ce projet intéressant et assez divertissant. En effet, même si le jeu fonctionne bien, il pourrait être amélioré et le code mieux structuré. J’ai ainsi développé des compétences en programmation, en logique et surtout en travail d’équipe. Pour améliorer le projet, j’ajouterais plus de niveaux et une meilleure interface. Le travail a été globalement inclusif.


