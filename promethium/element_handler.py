# promethium/element_handler.py

import pandas as pd
import os


class Element:
    """
    A class to represent a chemical element.
    Each attribute corresponds to a column in the CSV file.
    """

    def __init__(self, data_series):
        # data_series is a row from our pandas DataFrame
        for index, value in data_series.items():
            # Dynamically create attributes for the object
            # e.g., self.name = "Thorium", self.atomic_number = 90
            setattr(self, index, value)

    def __repr__(self):
        # A nice way to represent the object when you print it
        name = getattr(self, 'name', 'Unknown')
        symbol = getattr(self, 'symbol', '?')
        return f"<Element {name} ({symbol})>"


# This class will load the data and provide the search methods.
class ElementFinder:
    """
    A class to find chemical elements by name, symbol, or atomic number.
    It loads data from a CSV file into a pandas DataFrame for easy searching.

    """

    def __init__(self):
        self._df = None  # To store the DataFrame
        self._load_data()

    def _load_data(self):
        # Construct the path to the CSV file relative to this file's location
        base_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(base_dir, 'data', 'elements.csv')

        try:
            self._df = pd.read_csv(csv_path)
            # Make name lookups case-insensitive by creating a lowercase column
            self._df['name_lower'] = self._df['name'].str.lower()
            self._df['atomic_number'] = self._df.index + 1
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find elements.csv at {csv_path}")

    def name(self, element_name):
        """Looks up an element by its name (case-insensitive)."""
        result = self._df[self._df['name_lower'] == element_name.lower()]
        if result.empty:
            return None
        # Return an Element object created from the first matching row
        return Element(result.iloc[0])

    def symbol(self, element_symbol):
        """Looks up an element by its symbol."""
        result = self._df[self._df['symbol'] == element_symbol]
        if result.empty:
            return None
        return Element(result.iloc[0])

    def atomic_number(self, number):
        """Looks up an element by its atomic number."""
        result = self._df[self._df['atomic_number'] == number]
        if result.empty:
            return None
        return Element(result.iloc[0])
