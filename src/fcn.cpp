#include "fcn.h"

#include <cmath>
#include <numeric>  // std::accumulate
#include <iostream>

using namespace llfit;
using std::cout;
using std::endl;

double TheFCN::operator() (const std::vector<double>& par) const {
    m_driver.setParams(par[0], par[1], par[2], par[3], par[4]);

    const double data = std::accumulate(m_evts.begin(), m_evts.end(), 0.,
        [&](double& s, const Event& e) {return s + log(m_driver(e));});

    const double norm = std::accumulate(m_evtsNorm.begin(), m_evtsNorm.end(), 0.,
        [&](double& s, const Event& e) {return s + m_driver(e);});

    const double loglh = -data + log(norm) * m_evts.size();
    
    cout << "loglh: " << loglh << "  ";
    for (auto p : par) {
        cout << " " << p;
    }
    cout << endl;
    return loglh;
}
