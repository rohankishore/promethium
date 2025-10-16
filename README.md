<div align="center">
  <h1>Promethium 🧪</h1>
  <p>
    <strong>Unleash the elements. A Pythonic interface to a rich, offline database of chemical information.</strong>
  </p>
  <p>
    <a href="#"><img src="https://img.shields.io/pypi/v/promethium?style=for-the-badge&color=blueviolet" alt="PyPI version"></a>
    <a href="#"><img src="https://img.shields.io/badge/python-3.8+-blue.svg?style=for-the-badge" alt="Python version"></a>
    <a href="#"><img src="https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge" alt="License"></a>
    <a href="#"><img src="https://img.shields.io/github/workflow/status/rohankishore/promethium/CI?style=for-the-badge" alt="Build Status"></a>
  </p>
</div>

---

**Promethium** is your go-to periodic table and chemistry toolkit in Python. All data is included for **100% offline use**. No internet connection or API keys are required, making it fast, reliable, and perfect for any environment.

## ✨ Features

-   **Offline First**: All data is bundled with the library. No network calls, ever.
-   **Comprehensive Element Data**: Access dozens of properties for each element, from atomic mass to electronegativity.
-   **Chemical Equation Balancer**: Programmatically balance complex chemical reactions with a single function call.
-   **Intuitive API**: A clean, object-oriented interface that's a joy to use.
-   **Lightweight & Fast**: Built for performance using an efficient data-handling backend.


## 🚀 Installation

Install Promethium easily with pip:

```bash
pip install promethium
```

## 💡 Quick Start
Getting started with Promethium is incredibly simple.

Fetching Element Data
Look up any element by its name, symbol, or atomic number. The returned object gives you access to all its properties.

```python
from promethium import element

# Find an element by its name (case-insensitive)
thorium = element.name("Thorium")

if thorium:
    print(f"Name: {thorium.name}")
    print(f"Symbol: {thorium.symbol}")
    print(f"Atomic Mass: {thorium.atomic_mass}")
    print(f"Atomic Radius: {thorium.atomic_radius} pm")
    
# >>> Name: Thorium
# >>> Symbol: Th
# >>> Atomic Mass: 232.0377
# >>> Atomic Radius: 179 pm
```

### Balancing Chemical Equations
Provide lists of reactants and products, and let the balancer do the work, returning a dictionary of stoichiometric coefficients.

```python
from promethium import balance_equation

# Balance the formation of water
reactants = ['H2', 'O2']
products = ['H2O']

balanced = balance_equation(reactants, products)

print(f"Reactants: {balanced['reactants']}")
print(f"Products: {balanced['products']}")

# >>> Reactants: {'H2': 2, 'O2': 1}
# >>> Products: {'H2O': 2}
# This represents the equation: 2H₂ + O₂ ⟶ 2H₂O
```

## 🗺️ Roadmap
1. [ ] Isotope data integration
2. [ ] Compound property calculator (molecular weight, etc.)
3. [ ] Thermodynamic data module
4. [ ] 2D/3D molecule visualization hooks

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📄 License
This project is licensed under the MIT License.