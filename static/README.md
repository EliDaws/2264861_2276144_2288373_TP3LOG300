# static/

Ce dossier contient les fichiers statiques du frontend, c'est-à-dire les fichiers que Flask envoie
directement au navigateur sans les modifier.

## Fichiers

| Fichier     | Rôle                                                                                          |
|-------------|-----------------------------------------------------------------------------------------------|
| `style.css` | Style de la calculatrice : centrage de la page, écran, grille de boutons et couleurs des opérateurs. |

## Dépendances et hypothèses

- Le fichier est chargé par `templates/index.html` avec `url_for('static', filename='style.css')`.
  Si on renomme le fichier ou le dossier, il faut aussi changer le lien dans le template.
- Flask sert automatiquement le dossier `static/` à l'adresse `/static/`, donc aucune route n'est
  à ajouter dans `app.py`.
- Le CSS se base sur les classes et l'id utilisés dans le HTML (`.calculator`, `#display`,
  `.buttons`, `.btn`, `.operator`). Si on les change dans le template, il faut aussi les changer ici.
