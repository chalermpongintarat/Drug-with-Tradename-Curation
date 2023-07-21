with open("tradename_with_duplicate.txt", "r") as file: 
    lines = file.read().split("\n")

    tradename_remove_duplicate = []
    for line in lines:

        if line not in tradename_remove_duplicate:
            tradename_remove_duplicate.append(line)

    f = open("tradename_remove_duplicate.txt", "w")
    for line in tradename_remove_duplicate:
        f.write(str(line))
        f.write("\n")
    f.close()
