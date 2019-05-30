/** Von Neumann algorithm for event generation **/

#ifndef ACCEPTREJECT_H__
#define ACCEPTREJECT_H__

#include <vector>
#include <fstream>

#include "event.h"
#include "driver.h"
#include "rndm.h"

namespace llfit {

class AcceptReject {
    const Driver& m_driver;
    RndmD m_rndm;
    double m_maj;

 public:
    AcceptReject(const Driver& d, int seed=0, double maj=0.);

    bool run(const Event& evt);
    size_t run(const std::vector<Event>& evts, std::ofstream& ofile);
};

}  // namespace llfit

#endif  // ACCEPTREJECT_H__
