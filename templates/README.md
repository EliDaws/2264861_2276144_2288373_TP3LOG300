# templates/

Ce dossier contient les templates HTML (Jinja2) que Flask utilise pour générer les pages.

## Fichiers

| Fichier      | Rôle                                                                                       |
|--------------|--------------------------------------------------------------------------------------------|
| `index.html` | Interface de la calculatrice : l'écran, les boutons (chiffres, opérateurs, `C` et `=`) et le petit script JavaScript qui remplit ou vide l'écran. |

## Fonctionnement

1. Les boutons de chiffres et d'opérateurs appellent `appendToDisplay()`, qui ajoute le caractère
   à la fin de l'écran. Si l'écran affiche un résultat (après `=`), un chiffre vide d'abord l'écran
   pour commencer un nouveau calcul, alors qu'un opérateur continue le calcul à partir du résultat.
   Si le résultat est négatif, continuer le calcul donne une erreur, puisque `app.py` ne prend pas
   en charge les nombres négatifs.
   Après un message `Error: ...`, n'importe quel bouton repart d'un écran vide.
2. Le bouton `C` appelle `clearDisplay()` pour vider l'écran.
3. Le bouton `=` envoie le formulaire en POST à la route `/`. Le contenu de l'écran est envoyé dans
   le champ `display`.
4. `app.py` calcule le résultat et renvoie la page avec la variable `result`, qui est affichée dans
   l'écran.

## Dépendances et hypothèses

- Le template est rendu par la fonction `index()` de `app.py` avec `render_template('index.html', result=...)`.
- Le nom du champ `display` doit rester le même que celui lu dans `app.py`
  (`request.form.get('display')`).
- Le style vient de `static/style.css`.
- Le JavaScript est directement dans la page, il n'y a pas de fichier `.js` séparé.
