#ifndef CYL // header guards
#define CYL

namespace shapes {
    class Cyl {
        private:
        double height;
        double rad;
        public:
            Cyl();
            Cyl(double height, double rad);
            Cyl(const Cyl& obj);
            ~Cyl();
            double volume();
            double full_Square();
            double getHeight();
            void setHeight(double height);
            double getRad();
            void setRad(double rad);
    };
}
#endif
