def get_map():
    """Takes the input file and returns the lines as a 2D array

    A file is invalid and the program should end with an error message if...

    the file doesn't exist
    numRows are less than 1
    numCols are less than 1
    the start position is not within range
    """

    try:

        # Have the user enter an input file
        input_file = input("File name: ")

        with open(input_file, "r") as file:
            lines = file.readlines()

        lines = [line.strip() for line in lines]

        # Check rows columns and start position
        r, c = lines[0].split(" ")
        sr, sc = lines[1].split(" ")
        if int(r.strip()) < 1 or int(c.strip()) < 1 or int(sr.strip()) < 0 or int(sc.strip()) < 0:
            raise IndexError("Rows and/or columns must be greater than 0")
        if int(sr.strip())+1 > int(r.strip()) or int(sc.strip())+1 > int(c.strip()):
            raise IndexError("Start position must be within the maps bounds")

        return lines

    except FileNotFoundError:
        print("That file doesn't seem to exist.")
