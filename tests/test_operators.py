"""
Tests unitaires des fonctions de operators.py.

On vérifie que chaque opération donne le résultat attendu, autant avec des
entiers qu'avec des nombres décimaux ou négatifs.
"""

import pytest

from operators import add, subtract, multiply, divide


def test_add_entiers():
    """Vérifie l'addition de deux entiers positifs."""
    assert add(2, 3) == 5


def test_add_negatif_et_decimal():
    """Vérifie l'addition avec un nombre négatif et des décimaux."""
    assert add(-4, 1) == -3
    assert add(1.5, 2.25) == pytest.approx(3.75)


def test_subtract_entiers():
    """Vérifie que subtract(a, b) retourne a - b et pas b - a."""
    assert subtract(10, 4) == 6


def test_subtract_resultat_negatif():
    """Vérifie une soustraction dont le résultat est négatif."""
    assert subtract(3, 8) == -5


def test_multiply_entiers():
    """Vérifie la multiplication de deux entiers."""
    assert multiply(3, 4) == 12


def test_multiply_par_zero():
    """Vérifie que multiplier par 0 donne 0."""
    assert multiply(7, 0) == 0


def test_divide_exacte():
    """Vérifie une division qui tombe juste."""
    assert divide(10, 2) == 5


def test_divide_resultat_decimal():
    """Vérifie qu'une division garde la partie décimale (7 / 2 = 3.5)."""
    assert divide(7, 2) == pytest.approx(3.5)


def test_divide_par_zero():
    """Vérifie qu'une division par zéro lève une erreur au lieu de retourner un résultat."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
