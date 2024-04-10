class Point:

    def __init__(self, x, y):
        self.__coord_x = x
        self.__coord_y = y

    @property
    def coord_x(self):
        return self.__coord_x
    
    @coord_x.setter
    def coord_x(self, x):
        self.__coord_x = x

    @property
    def coord_y(self):
        return self.__coord_y

    @coord_y.setter
    def coord_y(self, y):
        self.__coord_y = y

    def get_coord(self):
        return self.__coord_x, self.__coord_y
    
    def set_coord(self, x, y):
        self.__coord_x = 10
        self.__coord_y = 10
    
p = Point(0, 1)
p.coord_x = 10


# p.set_coord(10, 10)
# d = p.get_coord()
# p.coord_x = 10


