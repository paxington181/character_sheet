import json

def main():

    with open("characters/Barbi McBarian.json", "r", encoding = "utf-8") as file:
        character = json.load(file)
        class_list:list = []
        level_sum:int = 0
        
        for i in range(0, len(character["char_class"])):
            printable = character["char_class"][i]
            print(printable)
            class_list.append(printable)
            level_sum += printable[1]
        print(class_list)
        print(level_sum)

main()