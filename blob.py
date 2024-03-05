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

    def teleport(self):
        """Goes from one sewer to another"""
        print("Teleport")

    def check_tile(self, x, y):
        tile = self.map[x][y]
        if tile == "P":
            self.people_eaten += 1
        elif tile == "@":
            self.teleport()

    def spread(self, x, y):
        """"""
        self.check_tile(x, y)
        # Check up, right, down, left
        if y > 0:
            "Can go up"
        elif x < self.max_x:
            "Can go right"
        elif y < self.max_y:
            "Can go down"
        elif x > 0:
            "Can go left"
        elif (x, y) in self.sewers:
            "Can travel through sewers"
        self.map[x][y] = "B"

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
