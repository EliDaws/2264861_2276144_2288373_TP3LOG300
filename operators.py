"""
Opérations arithmétiques de base utilisées par la calculatrice.

Chaque fonction reçoit deux nombres et retourne le résultat de l'opération.
Elles sont appelées par calculate() dans app.py.
"""

def add(a,b):
    """
    Additionne deux nombres.

    Args:
        a (float): le premier nombre.
        b (float): le deuxième nombre.

    Returns:
        float: la somme a + b.
    """
    return a + b

def subtract(a,b):
    """
    Soustrait le deuxième nombre du premier.

    Args:
        a (float): le nombre de départ.
        b (float): le nombre à soustraire.

    Returns:
        float: la différence a - b.
    """
    return a - b

def multiply(a,b):
    """
    Multiplie deux nombres.

    Args:
        a (float): le premier facteur.
        b (float): le deuxième facteur.

    Returns:
        float: le produit a * b.
    """
    return a * b

def divide(a,b):
    """
    Divise le premier nombre par le deuxième.

    Args:
        a (float): le dividende.
        b (float): le diviseur.

    Returns:
        float: le quotient a / b.
    """
    return a / b
