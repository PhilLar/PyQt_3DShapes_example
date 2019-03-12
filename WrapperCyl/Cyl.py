import math

class Cyl:
    # [init], [default init] and [copy init] put together
    def __init__(self, height: int = 5, rad: int = 5):
        self.height = height
        self.rad = rad
        print('ne proizoshlo copy')

    # destructor
    def __del__(self):
        print('Object {} was destructed'.format(self))

    # instance methods
    def calc_volume(self):
            return math.pi*pow(self.rad, 2)*self.height
        
    def calc_fullSquare(self):
            return 2*math.pi*self.rad*(self.rad+self.height)

if __name__ == '__main__': 
    c = None 
    c = Cyl(5,5)
    print(c)
    a = Cyl(c)
    print(a)
    # print(c)
    # print('kek')
    # d = Cyl(obj = c)
    # print(c.calc_volume())
    # print(c.calc_fullSquare())
    # print(c.height)
    # print(d.height)
    # c.height = 10
    # print(c.height)
    # print(d.height)
