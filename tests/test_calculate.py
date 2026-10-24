"""
Tests de la fonction calculate() de app.py.

On vérifie que les expressions valides donnent le bon résultat et que les
expressions invalides lèvent une ValueError.
"""

import pytest

from app import calculate


@pytest.mark.parametrize(
    "expression, attendu",
    [
        ("2+3", 5),
        ("10-4", 6),
        ("3*4", 12),
        ("8/2", 4),
        ("7/2", 3.5),
        ("1.5+2.5", 4),
    ],
)
def test_calculate_expressions_valides(expression, attendu):
    """Vérifie le résultat de chaque opérateur sur une expression simple."""
    assert calculate(expression) == pytest.approx(attendu)


def test_calculate_ignore_les_espaces():
    """Vérifie que les espaces autour de l'opérateur sont ignorés."""
    assert calculate(" 12 + 3 ") == 15


@pytest.mark.parametrize(
    "expression",
    [
        "",        # expression vide
        "123",     # aucun opérateur
        "+3",      # opérateur au début
        "3+",      # opérateur à la fin
        "2+3+4",   # plus d'un opérateur
        "a+2",     # opérande qui n'est pas un nombre
    ],
)
def test_calculate_expressions_invalides(expression):
    """Vérifie que les expressions mal formées lèvent une ValueError."""
    with pytest.raises(ValueError):
        calculate(expression)


def test_calculate_refuse_autre_chose_quune_chaine():
    """Vérifie qu'une valeur qui n'est pas une chaîne est refusée."""
    with pytest.raises(ValueError):
        calculate(None)
