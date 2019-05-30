#ifndef RNDMD_H__
#define RNDMD_H__

#include <cstdint>
#include <random>

/** @brief Random double generator (interface) */
class RndmD {
    double m_lo;  // lower bound
    double m_hi;  // upper bound
    static std::default_random_engine rng;
    std::uniform_real_distribution<double> rndm;

 public:
    /** Constructor takes the lower and upper bounds and 
        the initialization seed value */
    RndmD(double lo, double hi, int32_t seed = 0);
    /** Returs a random number uniformly distributed in the range */
    double operator()();
};

#endif  // RNDMD_H__
