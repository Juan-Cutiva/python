def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def writhe():
    names = ["Andres", "Miguel", "Pepe", "Juan", "Nicolle"]
    with open("./files/names.txt","a", encoding = "utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    writhe()


if __name__ == "__main__":
    run()