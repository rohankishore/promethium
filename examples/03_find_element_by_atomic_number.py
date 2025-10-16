from promethium.element_handler import ElementFinder

element_finder = ElementFinder()

# Find an element by its atomic number
element = element_finder.atomic_number(79)

if element:
    print(f"Name: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.atomic_number}")
