class Blob:

    def __init__(self, max_x, max_y, start_x, start_y, city_map):
        self.max_x = max_x
        self.max_y = max_y
        self.start_x = start_x
        self.start_y = start_y
        self.map = city_map
        self.sewers = []
        self.people_eaten = 0

    def find_sewers(self):
        for i, row in enumerate(self.map):
            for j, spot in enumerate(row):
                if spot == "@":
                    self.sewers.append((i, j))

    def spread(self):
        self.find_sewers()
        position = (self.start_x, self.start_y)
