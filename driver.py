"""
Author: Charlie Doherty
KUID: 3115329
Date: 2/28/24
Lab: 05
Last modified: 02/28/24
Purpose: Use recursion and backtracking to spread "The Blob" across a city

Run driver to execute the program
"""
from file_processor import get_map
from blob import Blob


def main():
    """The main function"""

    lines = get_map()
    max_x = lines[0].split(" ")[0]
    max_y = lines[0].split(" ")[1]
    start_x = lines[1].split(" ")[0]
    start_y = lines[1].split(" ")[1]
    city_map = lines[2:]

    my_blob = Blob(max_x, max_y, start_x, start_y, city_map)
    my_blob.spread()


if __name__ == "__main__":
    main()
