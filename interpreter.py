def main():
    expression = input("expression: ").strip()
    x , y , z = expression.split(" ")
    x = float(x)
    z = float(z)
    if y== "+":
        result= x + z
    elif y== "-":
        result= x - z
    elif y== "*":
        result= x * z
    elif y== "/":
        result= x / z
    print(result)
main()
