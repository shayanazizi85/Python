from fractions import Fraction as frac


def main():

    fuel = get_fraction("Fraction: ")

    if fuel >= 0 and fuel <= 1:
        print("E")

    if fuel >= 99 and fuel <= 100:
        print("F")

    if fuel > 1 and fuel <99:
        print(f"{fuel}%")

    else:
        if fuel < 0 or fuel > 100:
            main()


def get_fraction(prompt):

    while True:

        try:
            fuel = input(prompt)
            return round(frac(fuel) * 100)

        except (ValueError, ZeroDivisionError):
            pass


main()
