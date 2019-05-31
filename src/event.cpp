#include "event.h"

#include <cmath>

using namespace llfit;

inline double sinToCos(double s) {
    return sqrt(1. - s*s);
}

Event::Event(double cth, double cth1, double phi1, double cth2, double phi2) :
    c_data{cth, cth1, phi1, cth2, phi2},
    c_sinth1(sinToCos(cth1)), c_sinth2(sinToCos(cth2)),
    c_cosphi1(cos(phi1)), c_cosphi2(cos(phi2)),
    c_sinphi1(sinToCos(c_cosphi1)), c_sinphi2(sinToCos(c_cosphi2)),
    c_costhsq(cth*cth), c_sinthsq(1. - c_costhsq),
    c_sinth(sqrt(c_sinthsq)), c_sincosth(c_sinth * cth),
    c_f {
        1.,  // f0
        c_sinthsq * c_sinth1 * c_sinth2 * c_cosphi1 * c_cosphi2 + c_costhsq * cth1 * cth2,
        c_sincosth * (c_sinth1 * cth2 * c_cosphi1 + c_sinth2 * cth1 * c_cosphi2),
        c_sincosth * c_sinth1 * c_sinphi1,  // f3
        c_sincosth * c_sinth2 * c_sinphi2,  // f4
        c_costhsq,  // f5
        cth1 * cth2 - c_sinthsq * c_sinth1 * c_sinth2 * c_sinphi1 * c_sinphi2  // f6
    },
    c_g {
        cth * cth1,  // g1
        cth * cth2,  // g2
        c_sinth * c_sinth1 * c_cosphi1,  // g3
        c_sinth * c_sinth2 * c_cosphi2,  // g4
        c_sinth * (c_sinth1 * cth2 * c_sinphi1 + c_sinth2 * cth1 * c_sinphi2)  // g5
    }
    {}
