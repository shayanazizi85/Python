def convert(text : str):
    text = text.replace(":(","🙁")
    text = text.replace(":)","🙂")
    return text
def main():
    user_input = input("say something")
    print(convert(user_input))
main()
