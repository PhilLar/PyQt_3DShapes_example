cdef extern from "Cyl.h" namespace "shapes":

    cdef cppclass Cyl:
        # constructors
        Cyl() except +
        Cyl(double height, double rad) except +
        # instance methods
        double volume()
        double full_Square()
        double get_height()
        void set_height(double height)
        # setters&getters
        double getHeight()
        void setHeight(double height)
        double getRad()
        void setRad(double rad)


cdef class PyCyl:
    cdef Cyl* c_cyl

    # cinit contains both [constructor], [constructor by default] and [copy constructor]
    def __cinit__(self, height = None, rad = None, obj = None):
        if obj is not None and isinstance(obj, PyCyl):
            height = obj.getHeight()
            rad = obj.getRad()
            self.c_cyl = new Cyl(height, rad)
        elif height is not None and rad is not None:
            self.c_cyl = new Cyl(height, rad)
        else:
            self.c_cyl = new Cyl()

    # destructor
    def __dealloc__(self):
        del self.c_cyl


    def volume(self):
        val = self.c_cyl.volume()
        return val

    def full_Square(self):
        val = self.c_cyl.full_Square()
        return val

    def getHeight(self):
        val = self.c_cyl.getHeight()
        return val

    def setHeight(self, double height):
        self.c_cyl.setHeight(height)

    def getRad(self):
        val = self.c_cyl.getRad()
        return val

    def setRad(self, double rad):
        self.c_cyl.setRad(rad)


