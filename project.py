def greet(name: str) -> str:
    """
    Returns a friendly greeting based on the user's name.
    If the name is empty or contains only spaces, a generic greeting is returned.
    """
    name = str(name).strip()
    if not name:
        return "Hello!"
    return f"Hello, {name}! Nice to meet you."


def add(a, b):
    """
    Adds two values and returns the result.
    Works with numbers and strings, depending on user input.
    """
    return a + b


def analyze_list(values):
    """
    Analyzes a list and returns:
    - total number of items
    - number of unique items
    - whether the list contains a None value

    If input is not iterable, it will be treated as a single-element list.
    """
    if values is None:
        seq = []
    else:
        try:
            seq = list(values)
        except TypeError:
            seq = [values]

    return {
        "count": len(seq),
        "unique": len(set(seq)),
        "has_none": any(x is None for x in seq),
    }


def main():
    """
    A small interactive demo that runs when the program is executed.
    Demonstrates greeting, addition, and list analysis based on user input.
    """
    print("=== Simple Interactive Program ===")

    # Greeting section
    name = input("Enter your name: ").strip()
    print(greet(name))

    print("\n--- Addition Example ---")
    # Addition section
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        print("Result:", add(x, y))
    except ValueError:
        print("Invalid number! Skipping addition.")

    print("\n--- List Analysis ---")
    raw = input("Enter values separated by commas: ").strip()

    if raw:
        items = [
            item.strip() if item.strip() != "None" else None for item in raw.split(",")
        ]
    else:
        items = []

    result = analyze_list(items)
    print("List summary:", result)


if __name__ == "__main__":
    main()
