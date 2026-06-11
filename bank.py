welcome = input("please welcome").strip().lower()
if welcome.endswith(" ") or welcome.startswith(" "):
    print("$100")
elif welcome.startswith("hello"):
    print("$0")
elif welcome.startswith("h"):
    print("$20")
else:
    print("$100")
