class Point3D:
    def __init__(self, x, y, z):
        self.xyz = list()
        self.xyz.append(x)
        self.xyz.append(y)
        self.xyz.append(z)

    def set_x(self, x):
        self.xyz[0] = x

    def set_y(self, y):
        self.xyz[1] = y

    def set_z(self, z):
        self.xyz[2] = z

    def get(self):
        return self.xyz