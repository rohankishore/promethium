# promethium/__init__.py

# Import the main class from your handler file
from .element_handler import ElementFinder

# Create a single, accessible instance of the finder.
# When the user does "from promethium import element", they get this instance.
element = ElementFinder()