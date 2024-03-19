class Blob:
    """Class which uses a recursive backtracking function to traverse a map orthogonally"""

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

    def spread(self, r, c, back):
        """The recursive function that checks every direction"""
        # Go up
        if r > 0 and self.map[r - 1][c] != "#" and back != "up":
            self.spread(r - 1, c, "down")

        # Go right
        if c < self.max_x-1 and self.map[r][c+1] != "#" and back != "right":
            self.spread(r, c + 1, "left")

        # Go down
        if r < self.max_y-1 and self.map[r+1][c] != "#" and back != "down":
            self.spread(r + 1, c, "up")

        # Go left
        if c > 0 and self.map[r][c-1] != "#" and back != "left":
            self.spread(r, c - 1, "right")

        # Travel through sewer system
        if self.map[r][c] == "@" and len(self.sewers) != 0:
            r, c = self.sewers.pop()
            self.spread(r, c, "sewer")

        # After checking all directions mark current place as "B" unless it's a sewer
        if self.map[r][c] == "P":
            self.people_eaten += 1
            self.map[r][c] = "B"

        elif self.map[r][c] == "S":
            self.map[r][c] = "B"

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
        """Begins recursive call and returns a readable output"""
        self.spread(self.start_x, self.start_y, "None")
        return str(self)
