class city:
    def __init__(self, _lp, _x, _y):
        self.lp = int(_lp)
        self.x = float(_x)
        self.y = float(_y)

    def __str__(self):
        return "['" + str(self.lp) + "', '" + str(self.x) + "', '" + str(self.y) + "']"
    
    def __repr__(self):
        return "['" + str(self.lp) + "', '" + str(self.x) + "', '" + str(self.y) + "']"