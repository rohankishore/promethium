# test_script.py (place this in the promethium_project folder)

from promethium import element

# --- Look up by name ---
th = element.name("thorium")
if th:
    print(f"Found: {th.name}")
    print(f"Symbol: {th.symbol}")
    print(f"Atomic Number: {th.atomic_number}")
    # You can access any column from your CSV as an attribute!
    # For example, if you have a 'description' column:
    # print(f"Description: {th.description}")
    print("-" * 20)

# --- Look up by symbol ---
au = element.symbol("Au")
if au:
    print(f"Found: {au.name}")
    print(f"Atomic Mass: {au.atomic_mass}")
    print("-" * 20)

# --- Look up by atomic number ---
ten = element.atomic_number(10)
if ten:
    print(f"Found: {ten.name}")
    print(ten)  # Uses the __repr__ method we defined