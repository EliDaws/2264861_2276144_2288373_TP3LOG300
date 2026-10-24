"""
Point d'entrée de l'application Flask de la calculatrice.

Ce module crée le serveur Flask, s'occupe de lire l'expression envoyée par le
formulaire de la page web et de calculer le résultat avec les fonctions du
module operators.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

# Associe chaque symbole tapé dans la calculatrice à la fonction qui fait le calcul.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Évalue une expression simple de la forme "nombre opérateur nombre".

    Une seule opération est permise par expression (ex. "12+3" ou "4 / 2").
    Les espaces sont ignorés.

    Args:
        expr (str): l'expression entrée par l'utilisateur.

    Returns:
        float: le résultat de l'opération.

    Raises:
        ValueError: si l'expression est vide, contient plus d'un opérateur,
            n'a pas d'opérateur, a un opérateur au début ou à la fin, ou si
            les opérandes ne sont pas des nombres.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # On cherche l'opérateur et on refuse les expressions qui en ont plusieurs,
    # puisque la calculatrice ne gère qu'une opération à la fois.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Affiche la calculatrice et traite le calcul quand le formulaire est envoyé.

    En GET, la page est affichée avec un écran vide. En POST, l'expression
    du champ "display" est calculée et le résultat (ou le message d'erreur)
    est renvoyé dans la page.

    Returns:
        str: la page HTML générée à partir de templates/index.html.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            # L'erreur est affichée directement dans l'écran de la calculatrice
            # au lieu de faire planter la page.
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Le mode debug recharge le serveur automatiquement quand on modifie le code.
    app.run(debug=True)
