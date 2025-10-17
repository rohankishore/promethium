from promethium_py.element_handler import ElementFinder

element_finder = ElementFinder()

# Find an element by its name
element = element_finder.name("Gold")

if element:
    print(f"Name: {element.name}")
    print(f"Symbol: {element.symbol}")
    print(f"Atomic Number: {element.atomic_number}")
