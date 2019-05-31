#include "LLKine.h"

#include <cmath>
#include <iostream>

using std::array;

using linal::Vect;
using linal::LVect;

const Vect LLKine::c_ebeam(0., 0., 1.);

// Cosine of polar angle of Lambda in the global frame
double LLKine::cosLambda(const LVect& pr, const LVect& pin) {
    return dot(c_ebeam, (pr+pin).Vec().unit());
}

// Phi in [-pi, pi] from sin and cos
inline double angle(double cphi, double sphi) {
    return sphi > 0 ? acos(cphi) : -acos(cphi);
}

// Angles in the Lambda frame
array<double, 2> LLKine::omegaLambda(LVect pr, const LVect& pin) {
    LVect lamP4(pr + pin);
    Vect ez = lamP4.Vec().unit();
    Vect ey = cross(ez, c_ebeam).unit();
    Vect ex = cross(ey, ez).unit();
    Vect boost = -lamP4.BoostVec();
    Vect pdir = pr.Boost(boost).Vec().unit();
    auto tmp = pin;
    Vect pidir = tmp.Boost(boost).Vec().unit();

    Vect zero = pdir + pidir;
    if (zero.r2() > 0.00001) {
        std::cerr << zero << std::endl;
        throw(0);
    }

    double costh = dot(pdir, ez);
    double sinth = sqrt(1. - costh*costh);
    double sinphi = dot(pdir, ey) / sinth;
    double cosphi = dot(pdir, ex) / sinth;

    return {costh, angle(cosphi, sinphi)};
}

// Complete five phase space parameters
array<double, 5> LLKine::xi(const LVect& pr, const LVect& pin, const LVect& pbar, const LVect& pip) {
    auto om1 = omegaLambda(pr, pin);
    auto om2 = omegaLambda(pbar, pip);
    return {cosLambda(pr, pin), om1[0], om1[1], om2[0], om2[1]};
}
