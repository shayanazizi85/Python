month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
def main():
    while True:
        try:
            userInput = input("Date :")
            userInput = userInput.strip()
            if userInput[0:1].isdigit():
                m,d,y = userInput.split("/")
                m = m.strip()
                if len(y) == 4 and int(m) <= 12 and int(d) <= 12:
                    print(f"{int(y.strip())}-{int(m):02}-{int(d):02}")
                    break
                else:
                    continue
            else:
                day = userInput[-8:-6]
                year = userInput[-5:]
                monthnum = find_month(userInput, month) + 1
                if int(day) <= 31:
                    print(f"{year.strip()}-{monthnum:02}-{int(day):02}")
                    break
                else:
                    continue
        except (TypeError, ValueError):
            pass
        else:
            continue

def find_month(inp, lst):
    for i in month:
        if inp.startswith(i):
            while True:
                try:
                    index = lst.index(i)
                    return int(index)
                except ValueError:
                    pass
                else:
                    break
        else:
            continue
main()
