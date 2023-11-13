import sys

def fcopy(file1, file2):
    with open(file1, "rt"):
        with open(file2, "wt"):
            l1 = file1.readlines()
            for line in l1:
                file2.write(line)

def main():
    if sys.argv[0] == "fcopy.py":
        if len(sys.argv) == 1 or len(sys.argv) == 2:
            print("Usage: fcopy.py <src> <dest>")

main()