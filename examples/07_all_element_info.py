from promethium.element_handler import ElementFinder

element_finder = ElementFinder()

# Get all information for an element
element = element_finder.name("Uranium")

if element:
    for key, value in element.__dict__.items():
        print(f"{key}: {value}")
