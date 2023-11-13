import sys

def fcopy(file1, file2):
    with open(file1, "rt") as f: 
        with open(file2, "wt") as f_new:
            l1 = f.readlines()
            for line in l1:
                f_new.write(line)

def main():
    if sys.argv[0] == "fcopy.py":
        if len(sys.argv) == 1 or len(sys.argv) == 2:
            print("Usage: fcopy.py <src> <dest>")

if __name__ == "__main__":
    main()  