#include "rndm.h"

#include <chrono>  // seed generator

std::default_random_engine RndmD::rng;

RndmD::RndmD(double lo, double hi, int32_t seed) :
    m_lo(lo), m_hi(hi), rndm(m_lo, m_hi) {
    if (!seed)
        rng.seed(std::chrono::high_resolution_clock::now().time_since_epoch().count());
    else rng.seed(seed);
}

double RndmD::operator()() {
    return rndm(rng);
}
