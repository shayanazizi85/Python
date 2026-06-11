def main():
    # Syntax of dict = {'key': value}
    user_fruits = {}
    # Infinite loop with break
    while True:
        try:
            fruit = input().upper()  # Read input and convert to uppercase
            # Search if fruit matches a key inside the dict
            if fruit in user_fruits:
                user_fruits[fruit] += 1  # Increment count if fruit exists in dict
            else:
                user_fruits[fruit] = 1  # Add fruit to dict with count of 1 if it doesn't exist
        except EOFError:  # Catch EOFError to handle end of input
            # Sort and print the items of the dictionary
            for item in sorted(user_fruits):  # Sort keys of dict alphabetically
                print(user_fruits[item], item)  # Print count and fruit name
            break  # Break out of the loop when EOFError is raised
main()
