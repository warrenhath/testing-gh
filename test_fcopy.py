import fcopy as fc

test1 = fc.fcopy("input1.txt")

with open("input1.txt", "rt") as file:
    with open(test1, "rt") as filecopy:
        l = file.readlines()
        lcopy = filecopy.readlines()
        for line in range(len(l)):
            if l[line] != lcopy[line]:
                print("lines do not match")
                break
        print("Files match. Good job!")