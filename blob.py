class Blob:

    def __init__(self, max_x, max_y, start_x, start_y, city_map):
        self.max_x = int(max_x)
        self.max_y = int(max_y)
        self.start_x = int(start_x)
        self.start_y = int(start_y)
        self.people_eaten = 0

        # Create 2D array representing the city
        self.map = city_map
        for i, row in enumerate(self.map):
            new_row = []
            for col in row:
                new_row.append(col)
            self.map[i] = new_row

        # Get sewer locations
        self.sewers = []
        for i, row in enumerate(self.map):
            for j, spot in enumerate(row):
                if spot == "@":
                    self.sewers.append((i, j))

    def check_tile(self, row, col):
        tile = self.map[row][col]
        if tile == "P":
            self.people_eaten += 1
            return False
        elif tile == "@":
            return True

    def spread(self, r, c):
        """"""
        # todo: Need a way to mark past travel
        on_sewer = self.check_tile(r, c)

        # Can go up
        if r > 0 and self.map[r-1][c] != "#" and self.map[r-1][c] != "B":
            self.map[r][c] = "B"
            r -= 1
            self.spread(r, c)

        # Can go right
        elif c < self.max_x-1 and self.map[r][c+1] != "#" and self.map[r][c+1] != "B":
            self.map[r][c] = "B"
            c += 1
            self.spread(r, c)

        # Can go down
        elif r < self.max_y-1 and self.map[r+1][c] != "#" and self.map[r+1][c] != "B":
            self.map[r][c] = "B"
            r += 1
            self.spread(r, c)

        # Can go left
        elif c > 0 and self.map[r][c-1] != "#" and self.map[r][c-1] != "B":
            self.map[r][c] = "B"
            c -= 1
            self.spread(r, c)

        # Go through sewers
        elif on_sewer:
            self.map[r][c] = "B"
            r, c = self.sewers.pop(0)
            self.spread(r, c)

        # If the blob can't spread, mark a B and go back
        else:
            self.map[r][c] = "B"
            return

    def __str__(self):
        """Returns a well formatted map with the people eaten"""
        city = ""
        for row in self.map:
            for col in row:
                city += col
            city += "\n"
        city += f"People eaten: {self.people_eaten}"
        return city

    def output(self):
        self.spread(self.start_x, self.start_y)
        return str(self)
