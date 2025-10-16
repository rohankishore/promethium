from promethium.element_handler import ElementFinder

element_finder = ElementFinder()

# Get an element
element = element_finder.name("Iron")

if element:
    # You can access any of the properties from the CSV file
    print(f"Name: {element.name}")
    print(f"Atomic Mass: {element.atomic_weight}")
    print(f"Density: {element.density}")
    print(f"Melting Point: {element.fusion_heat}")
    print(f"Boiling Point: {element.evaporation_heat}")
