/** **/

#ifndef DRIVER_H__
#define DRIVER_H__

#include <array>

#include "event.h"

namespace llfit {

class Driver {
    double m_xi;  // electrons polarization level
    std::array<double, 7> m_fcoef;
    std::array<double, 5> m_gcoef;

 public:
    // explicit Driver() = default;
    Driver(double alp, double dphi, double alp1, double alp2, double xi);
    double operator() (const Event& evt) const;
    void setParams(double alp, double dphi, double alp1, double alp2, double xi);
};

}  // namespace llfit

#endif  // DRIVER_H__
