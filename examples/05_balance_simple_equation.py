from promethium.balancer import balance_equation

# Balance a simple equation
reactants = ['H2', 'O2']
products = ['H2O']

balanced_equation = balance_equation(reactants, products)

print(f"Reactants: {balanced_equation['reactants']}")
print(f"Products: {balanced_equation['products']}")
