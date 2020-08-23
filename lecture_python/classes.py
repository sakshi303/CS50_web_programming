class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


point = point(3,9)
print(point.x)
print(point.y)
point.y = int(point.y)
point.x = int(point.x)
print( point.x *point.y)