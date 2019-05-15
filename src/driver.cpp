#include "driver.h"

#include <cmath>
#include <numeric>  // std::inner_product
#include <iostream>

using namespace llfit;

Driver::Driver(double alp, double dphi, double alp1, double alp2, double xi) {
    setParams(alp, dphi, alp1, alp2, xi);
}

double Driver::operator() (const Event& evt) const {
    // std::cout << "Driver::operator" << std::endl;
    const double a = std::inner_product(m_fcoef.begin(), m_fcoef.end(), evt.f().begin(), 1.);
    // std::cout << "a = " << a << std::endl;
    const double b = std::inner_product(m_gcoef.begin(), m_gcoef.end(), evt.g().begin(), 1.);
    // std::cout << "b = " << b << std::endl;
    if (a + m_xi * b < 0)
        std::cout << "a + m_xi * b = " << a + m_xi * b << std::endl;
    return a + m_xi * b;
}

void Driver::setParams(double alp, double dphi, double alp1, double alp2, double xi) {
    // TODO: add checks
    m_xi = xi;
    const double sindphi = sin(dphi);
    const double cosdphi = cos(dphi);
    const double aa12 = alp1 * alp2;
    const double squmasq = sqrt(1. - alp*alp);
    m_fcoef = {
        1.,  // f0
        aa12,  // f1
        aa12 * squmasq * cosdphi,  // f2
        squmasq * sindphi * alp1,  // f3
        squmasq * sindphi * alp2,  // f4
        alp,  // f5
        aa12 * alp  // f6
    };
    m_gcoef = {
        (1. + alp) * alp1,  // g1
        (1. + alp) * alp2,  // g2
        squmasq * cosdphi * alp1,  // g3
        squmasq * cosdphi * alp2,  // g4
        squmasq * aa12 * sindphi  // g5
    };
}
