def get_map():
    """Takes the input file and returns the lines as a 2D array"""
    while True:
        try:

            # Have the user enter an input file
            input_file = input("File name: ")

            with open(input_file, "r") as file:
                lines = file.readlines()

            lines = [line.strip() for line in lines]

            return lines

        except FileNotFoundError:
            print("That file doesn't seem to exist.")
