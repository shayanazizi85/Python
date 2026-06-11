vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
vowel_remove = input("Input: ")
print("Output: ", end="")

output = ""
for char in vowel_remove:
    if char in vowel:
        continue
    else:
        output += char
print(output)
