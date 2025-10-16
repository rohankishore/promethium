from promethium.element_handler import ElementFinder

element_finder = ElementFinder()

# Find an element by its symbol
element = element_finder.symbol("Ag")

if element:
    print(f"Name: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.atomic_number}")
