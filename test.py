from promethium.balancer import balance_equation
from promethium.element_handler import ElementFinder

# --- Test element finder ---
element_finder = ElementFinder()

th = element_finder.name("thorium")
if th:
    print("--- Element Information ---")
    for key, value in th.__dict__.items():
        print(f"{key}: {value}")
    print("-" * 20)

print(th.atomic_radius)


# --- Test balancer ---
reactants = ['H2', 'O2']
products = ['H2O']

balanced_equation = balance_equation(reactants, products)

print("--- Balanced Equation ---")
print(f"Reactants: {balanced_equation['reactants']}")
print(f"Products: {balanced_equation['products']}")