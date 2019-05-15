#include "acceptReject.h"

#include <iostream>

using namespace llfit;

AcceptReject::AcceptReject(const Driver& d, int seed, double maj) : 
    m_driver(d), m_rndm(0., 1., seed), m_maj(maj) {}

bool AcceptReject::run(const Event& evt) {
    return m_driver(evt) > m_rndm() * m_maj;
}

size_t AcceptReject::run(const std::vector<Event>& evts, std::ofstream& ofile) {
    std::vector<double> pdf(evts.size());
    m_maj = 0.;
    auto pdfit = pdf.begin();
    for (auto& e : evts) {
        *pdfit = m_driver(e);
        if (m_maj < *pdfit) {
            m_maj = *pdfit;
        }
        pdfit++;
    }

    std::cout << "Majorant: " << m_maj << std::endl;

    size_t counter = 0;
    pdfit = pdf.begin();
    for (auto& e : evts) {
        if (*pdfit > m_rndm() * m_maj) {
            ofile << e << std::endl;
            counter++;
        }
    }

    return counter;
}
