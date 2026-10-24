"""
Tests de la route Flask et de l'interface (templates/index.html).

On envoie des requêtes avec le client de test pour vérifier que la page
s'affiche, que le résultat revient dans l'écran et que les boutons affichent
la bonne valeur.
"""

import re

import pytest


def test_page_accueil_s_affiche(client):
    """Vérifie que la page principale répond avec un code 200 et contient la calculatrice."""
    reponse = client.get("/")
    assert reponse.status_code == 200
    assert b"Flask Calculator" in reponse.data


def test_post_affiche_le_resultat(client):
    """Vérifie que le résultat du calcul est renvoyé dans l'écran après un POST."""
    reponse = client.post("/", data={"display": "2+3"})
    assert reponse.status_code == 200
    assert b'value="5.0"' in reponse.data


def test_post_expression_invalide_affiche_erreur(client):
    """Vérifie qu'une expression invalide affiche un message d'erreur au lieu de planter."""
    reponse = client.post("/", data={"display": "2+"})
    assert reponse.status_code == 200
    assert b"Error:" in reponse.data


def test_post_division_par_zero_affiche_erreur(client):
    """Vérifie qu'une division par zéro affiche une erreur au lieu de planter la page."""
    reponse = client.post("/", data={"display": "5/0"})
    assert reponse.status_code == 200
    assert b"Error:" in reponse.data


def _boutons_de_saisie(html):
    """
    Trouve tous les boutons qui ajoutent un caractère à l'écran.

    Args:
        html (str): le HTML de la page.

    Returns:
        list[tuple[str, str]]: pour chaque bouton, la valeur ajoutée à l'écran
        et le texte affiché sur le bouton.
    """
    return re.findall(r"appendToDisplay\('(.)'\)\">([^<]*)</button>", html)


def test_page_contient_tous_les_boutons(client):
    """Vérifie qu'il y a un bouton pour chaque chiffre et chaque opérateur."""
    html = client.get("/").get_data(as_text=True)
    valeurs = {valeur for valeur, _ in _boutons_de_saisie(html)}
    assert valeurs == set("0123456789+-*/")


@pytest.mark.parametrize("valeur", list("0123456789+-*/"))
def test_texte_du_bouton_correspond_a_sa_valeur(client, valeur):
    """
    Vérifie que le texte affiché sur chaque bouton est la valeur qu'il ajoute à l'écran.

    Sinon l'utilisateur ne sait pas sur quoi il clique.
    """
    html = client.get("/").get_data(as_text=True)
    boutons = dict(_boutons_de_saisie(html))
    assert boutons[valeur].strip() == valeur
