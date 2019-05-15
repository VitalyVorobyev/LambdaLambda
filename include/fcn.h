/** **/

#ifndef FCN_H__
#define FCN_H__

#include <vector>

#include "Minuit2/FCNBase.h"

#include "event.h"
#include "driver.h"

namespace llfit {

class TheFCN : public ROOT::Minuit2::FCNBase {
    Driver& m_driver;
    const std::vector<Event>& m_evts;
    const std::vector<Event>& m_evtsNorm;

 public:
    TheFCN(Driver& d, std::vector<Event>& evt,
            std::vector<Event>& norm) : 
        m_driver(d), m_evts(evt), m_evtsNorm(norm) {}

    double operator() (const std::vector<double>& par) const override;
    double Up() const override {return 0.5;}
};

}  // namespace llfit

#endif  // FCN_H__
