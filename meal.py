def main():
    time = input("please enter time: ")
    test = convert(time)
    if 7 <= test <= 8:
        print("breakfast time")
    elif 12 <= test <= 13:
        print("lunch time")
    elif 18 <= test <= 19:
        print("dinner time")
    else:
        print("")
def convert(time):
    hours , minuts = time.split(":")
    return float(hours) + float(minuts) / 60


if __name__ == "__main__":
    main()
