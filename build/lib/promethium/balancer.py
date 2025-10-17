import re
import numpy as np
from collections import Counter


def balance_equation(reactants, products):
    """
    Balances a chemical equation using a custom algorithm.

    Args:
        reactants (list): A list of strings representing the reactants.
        products (list): A list of strings representing the products.

    Returns:
        dict: A dictionary containing the balanced coefficients for the reactants and products.
    """

    def parse_formula(formula):
        """Parses a chemical formula and returns a dictionary of atom counts."""
        pairs = re.findall(r'([A-Z][a-z]*)(\d*)', formula)
        counts = Counter()
        for element, count in pairs:
            count = int(count) if count else 1
            counts[element] += count
        return counts

    reactant_formulas = [parse_formula(f) for f in reactants]
    product_formulas = [parse_formula(f) for f in products]

    all_elements = sorted(
        list(set(k for f in reactant_formulas for k in f.keys()) | set(k for f in product_formulas for k in f.keys())))

    num_reactants = len(reactant_formulas)
    num_products = len(product_formulas)
    num_elements = len(all_elements)

    matrix = np.zeros((num_elements, num_reactants + num_products))

    for i, element in enumerate(all_elements):
        for j, formula in enumerate(reactant_formulas):
            matrix[i, j] = formula.get(element, 0)
        for j, formula in enumerate(product_formulas):
            matrix[i, j + num_reactants] = -formula.get(element, 0)

    # Add a row to the matrix to constrain the solution
    matrix = np.vstack([matrix, np.ones(num_reactants + num_products)])
    b = np.zeros(num_elements + 1)
    b[-1] = 1

    # Use least squares to find a solution
    coeffs, _, _, _ = np.linalg.lstsq(matrix, b, rcond=None)

    # Find the smallest integer coefficients
    multiple = 1
    while not np.all(np.isclose(coeffs * multiple, np.round(coeffs * multiple))):
        multiple += 1

    coeffs = np.round(coeffs * multiple).astype(int)

    return {
        'reactants': dict(zip(reactants, coeffs[:num_reactants])),
        'products': dict(zip(products, coeffs[num_reactants:])),
    }
