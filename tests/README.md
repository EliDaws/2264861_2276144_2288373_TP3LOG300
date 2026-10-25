# tests/

Ce dossier contient les tests automatisés du projet. Ils sont écrits avec `pytest`.

## Lancer les tests

À partir de la racine du dépôt (avec l'environnement virtuel activé si vous en utilisez un) :

```bash
pip install flask pytest
python -m pytest
```

Pour avoir le détail de chaque test :

```bash
python -m pytest -v
```

Pour lancer un seul fichier ou un seul test :

```bash
python -m pytest tests/test_operators.py
python -m pytest tests/test_operators.py::test_subtract_entiers
```

## Fichiers

| Fichier             | Ce qui est testé                                                                 |
|---------------------|----------------------------------------------------------------------------------|
| `conftest.py`       | Configuration commune : ajoute la racine du dépôt au chemin de Python et fournit le client de test Flask (`client`). |
| `test_operators.py` | Les fonctions `add`, `subtract`, `multiply` et `divide` de `operators.py` (entiers, décimaux, négatifs, division par zéro). |
| `test_calculate.py` | La fonction `calculate()` de `app.py` : expressions valides pour chaque opérateur, espaces ignorés et expressions invalides qui doivent lever une `ValueError`. |
| `test_app.py`       | La route `/` et l'interface : affichage de la page, résultat renvoyé dans l'écran, messages d'erreur, et texte de chaque bouton qui doit correspondre à la valeur ajoutée à l'écran. |

## Ce qui n'est pas couvert

- Le JavaScript de la page (`appendToDisplay()` et `clearDisplay()`) n'est pas exécuté par les
  tests, puisqu'il faudrait un vrai navigateur. On vérifie seulement que les boutons sont bien
  présents dans le HTML. Ce comportement est donc vérifié à la main (voir plus bas).
- Le style CSS n'est pas testé.

## Vérification manuelle

Le comportement de l'écran après `=` (issue #11) est géré par le JavaScript, donc il se vérifie
dans le navigateur. Lancer `python app.py`, ouvrir <http://127.0.0.1:5000>, puis :

| Étapes                              | Résultat attendu                                   |
|-------------------------------------|----------------------------------------------------|
| `2`, `+`, `3`, `=`, puis `4`        | L'écran affiche `4` (nouveau calcul).              |
| `2`, `+`, `3`, `=`, puis `+`, `2`   | L'écran affiche `5.0+2` (le calcul continue).      |
| `2`, `+`, `=`, puis `+`             | Le message `Error: ...` est effacé, l'écran affiche `+`. |
| `2`, `+`, `3`, `=`, puis `C`, `4`   | L'écran affiche `4`.                               |

## Hypothèses

- Les tests utilisent le client de test de Flask, donc il n'est pas nécessaire de lancer le serveur
  avant de les exécuter.
- Les résultats décimaux sont comparés avec `pytest.approx` pour éviter les problèmes d'arrondi des
  nombres à virgule flottante.
