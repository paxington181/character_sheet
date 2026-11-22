import json

def main():

    with open("characters/Barbi McBarian.json", "r", encoding = "utf-8") as file:
        character = json.load(file)
        for i in range(0, len(character["char_class"])):
            printable = character["char_class"][i]
            print(printable)


main()