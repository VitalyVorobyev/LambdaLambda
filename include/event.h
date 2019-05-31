/** The Event class **/

#ifndef EVENT_H__
#define EVENT_H__

#include <array>
#include <iostream>
#include <fstream>

namespace llfit {

class Event {
    const std::array<double, 5> c_data;
    const double c_sinth1;
    const double c_sinth2;
    const double c_cosphi1;
    const double c_cosphi2;
    const double c_sinphi1;
    const double c_sinphi2;
    const double c_costhsq;  // cos**2(th)
    const double c_sinthsq;  // sin**2(th)
    const double c_sinth;
    const double c_sincosth;  // sin(th) * cos(th)
    const std::array<double, 7> c_f;  // polarization-independent structure functions
    const std::array<double, 5> c_g;  // polarization-dependent structure functions

 public:
    Event(double cth, double cth1, double phi1, double cth2, double phi2);

    const auto& f() const {return c_f;}
    const auto& g() const {return c_g;}

    friend std::ostream& operator<<(std::ostream& o, const Event& e) {
        for (auto& d : e.c_data) {
            o << d << " ";
        }
        return o;
    }

    friend std::ofstream& operator<<(std::ofstream& o, const Event& e) {
        for (auto& d : e.c_data) {
            o << d << " ";
        }
        return o;
    }
};

}  // namespace llfit

#endif  // EVENT_H__
