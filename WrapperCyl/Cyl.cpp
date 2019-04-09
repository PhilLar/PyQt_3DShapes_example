#include "Cyl.h"
#include <cmath>
#include <iostream>
using namespace std;

namespace shapes {

	Cyl::Cyl() {
        this->height = 5;
	    this->rad = 5;
    }

	Cyl::Cyl(double height, double rad) {
		this->height = height;
		this->rad = rad;
	}

	Cyl::Cyl(const Cyl& obj) {
		this->height = obj.height;
		this->rad = obj.rad;
	}

	Cyl::~Cyl() {
		cout << "object was destructed" << endl;
	}


	double Cyl::volume() {
		return 3.14*pow(rad, 2)*height;
	}

	double Cyl::full_Square() {
		return 2 * 3.14*rad*height + 2 * 3 / 14 * pow(rad, 2);
	}

    double Cyl::getHeight() {
        return height;
    }

    void Cyl::setHeight(double height) {
        Cyl::height = height;
    }

	double Cyl::getRad() {
        return rad;
    }

    void Cyl::setRad(double rad) {
        Cyl::rad = rad;
    }
}
