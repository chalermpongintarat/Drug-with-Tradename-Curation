with open("list_of_tradename.txt", "r") as file: 
    lines = file.read().split("\n")

    all_tradename = []
    for line in lines:
        all_tradename.append(line)

    all_tradename = ', '.join(all_tradename)

    f = open("all_tradename.txt", "w")
    f.write(str(all_tradename))
    f.close()