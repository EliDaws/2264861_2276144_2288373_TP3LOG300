# Calculatrice Flask - TP3 LOG3000

Travail pratique 3 du cours LOG3000.

## Équipe 10

- 2264861
- 2276144
- 2288373

## Description du projet

Le projet est une calculatrice web simple faite en Python avec Flask. L'utilisateur construit une
opération avec les boutons de l'interface et le serveur calcule le résultat, qui s'affiche ensuite
dans l'écran de la calculatrice.

### Portée

La calculatrice permet de :

- faire une addition (`+`), une soustraction (`-`), une multiplication (`*`) ou une division (`/`) ;
- utiliser des nombres entiers ou décimaux ;
- afficher un message d'erreur si l'expression n'est pas valide.

Ce que la calculatrice ne fait pas :

- une seule opération est permise à la fois (`2+3` fonctionne, mais pas `2+3*4`) ;
- il n'y a pas de parenthèses, de nombres négatifs au début de l'expression ni de fonctions
  avancées (racine, puissance, etc.) ;
- il n'y a pas d'historique des calculs.

Le but du TP est aussi de mettre de l'ordre dans le projet : configurer le dépôt GitHub, documenter
le code, ajouter des tests et corriger les bogues en utilisant des issues, des branches et des pull
requests.

## Structure du projet

```
.
├── app.py            # Serveur Flask, route principale et fonction calculate()
├── operators.py      # Fonctions add, subtract, multiply et divide
├── static/
│   ├── style.css     # Style de la calculatrice
│   └── README.md
├── templates/
│   ├── index.html    # Interface de la calculatrice
│   └── README.md
└── README.md
```

### Backend (racine du dépôt)

- `app.py` : crée l'application Flask et définit la route `/`. La fonction `calculate()` reçoit
  l'expression, trouve l'opérateur, convertit les deux opérandes en nombres et appelle la bonne
  fonction de `operators.py`. Le dictionnaire `OPS` fait le lien entre chaque symbole et sa
  fonction.
- `operators.py` : contient les quatre opérations de base. Chaque fonction prend deux nombres et
  retourne le résultat.

Les dossiers `static/` et `templates/` ont chacun leur propre README qui explique leur contenu.

## Prérequis

Avant d'installer le projet, il faut avoir :

- Git
- Python 3
- pip
- Flask

## Installation

1. Cloner le dépôt :

   ```bash
   git clone git@github.com:EliDaws/2264861_2276144_2288373_TP3LOG300.git
   cd 2264861_2276144_2288373_TP3LOG300
   ```

2. (Optionnel, mais recommandé) Créer et activer un environnement virtuel :

   ```bash
   python -m venv venv
   source venv/bin/activate      # Sur Windows : venv\Scripts\activate
   ```

3. Installer Flask :

   ```bash
   pip install flask
   ```

4. Vérifier que Flask est bien installé :

   ```bash
   python -c "import flask; print(flask.__version__)"
   ```

## Utilisation

1. Lancer le serveur à partir de la racine du dépôt :

   ```bash
   python app.py
   ```

2. Ouvrir <http://127.0.0.1:5000> dans un navigateur.

3. Utiliser la calculatrice :
   - cliquer sur les chiffres et sur un opérateur pour construire l'expression (ex. `12+3`) ;
   - cliquer sur `=` pour obtenir le résultat ;
   - après le résultat, taper un chiffre commence un nouveau calcul, alors qu'un opérateur
     continue le calcul à partir du résultat (ex. `5.0` puis `+2` donne `5.0+2`). Comme les
     nombres négatifs ne sont pas pris en charge, un résultat négatif (ex. `-3.0`) ne peut pas
     être réutilisé : il faut commencer un nouveau calcul ;
   - cliquer sur `C` pour vider l'écran.

4. Si l'expression n'est pas valide (ex. deux opérateurs ou un opérateur à la fin), un message
   `Error: ...` s'affiche dans l'écran. Cliquer ensuite sur n'importe quel bouton efface le
   message et commence un nouveau calcul.

5. Pour arrêter le serveur, faire `Ctrl+C` dans le terminal.

## Tests

Les tests sont dans le dossier `tests/` et utilisent `pytest`.

1. Installer pytest :

   ```bash
   pip install pytest
   ```

2. Lancer tous les tests à partir de la racine du dépôt :

   ```bash
   python -m pytest
   ```

3. Pour lancer un seul fichier de test :

   ```bash
   python -m pytest tests/<nom_du_fichier>.py
   ```

Le détail de ce que couvrent les tests est dans le README du dossier `tests/`.

## Flux de contribution

On utilise le flux suivant pour toutes les modifications :

1. **Issues** : chaque bogue ou nouvelle fonctionnalité a sa propre issue sur GitHub. L'issue
   décrit le problème, les étapes pour le reproduire (ou le test qui échoue) et elle est assignée
   à un membre de l'équipe.

2. **Branches** : on ne travaille jamais directement sur `main`. Pour chaque issue, on crée une
   branche à partir de `main` directement dans l'issue sur GitHub (section **Development** →
   **Create a branch**). GitHub nomme la branche avec le numéro et le titre de l'issue, sous la
   forme `<numero-issue>-<titre-de-l-issue>`.

   Exemple : `1-subtract-inverse-lordre-des-opérandes`.

   On récupère ensuite la branche localement :

   ```bash
   git fetch
   git switch <numero-issue>-<titre-de-l-issue>
   ```

3. **Commits** : les messages de commit expliquent ce qui a été changé et pourquoi. On peut faire
   référence à l'issue avec son numéro (ex. `fix: corrige l'ordre des opérandes dans subtract (#1)`).

4. **Tests** : avant d'ouvrir une pull request, on relance tous les tests pour vérifier que le
   correctif fonctionne et qu'il ne brise rien d'autre.

5. **Pull requests** : on pousse la branche et on ouvre une pull request vers `main`. La
   description fait le lien avec l'issue (ex. `Closes #3`) pour qu'elle se ferme automatiquement
   lors de la fusion.

6. **Revue et fusion** : un autre membre de l'équipe relit la pull request avant de la fusionner
   dans `main`.
