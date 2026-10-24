"""
Configuration commune à tous les tests.

Ajoute la racine du dépôt au chemin de Python pour pouvoir importer app.py et
operators.py, peu importe d'où pytest est lancé. Fournit aussi un client de
test Flask pour les tests de la route.
"""

import os
import sys

import pytest

# Sans ça, "import app" ne fonctionne pas si on lance pytest à partir du dossier tests/.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app as flask_app


@pytest.fixture
def client():
    """
    Crée un client de test Flask pour envoyer des requêtes sans lancer le serveur.

    Returns:
        FlaskClient: le client de test de l'application.
    """
    flask_app.config["TESTING"] = True
    with flask_app.test_client() as client:
        yield client
