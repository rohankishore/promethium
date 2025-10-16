from promethium.balancer import balance_equation

# Balance a more complex equation
reactants = ['Fe2(SO4)3', 'KOH']
products = ['K2SO4', 'Fe(OH)3']

balanced_equation = balance_equation(reactants, products)

print(f"Reactants: {balanced_equation['reactants']}")
print(f"Products: {balanced_equation['products']}")
