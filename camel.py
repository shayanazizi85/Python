def main():
    camel=input("text:")
    snake=""
    for a in camel:
        if a.isupper():
            snake+="_"+a.lower()
        else:
            snake+=a
    print(snake)
main()
