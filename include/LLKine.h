/** Kinematic tools for J/psi -> [Lambda -> p pi-] [anti-Lambda -> pbar pi+]
 * 
 *  Coded by V. Vorobyev (BINP)
 *
 *  Date: 25 April 2019
 *
 **/

#ifndef LLKINE_H__
#define LLKINE_H__

#include <array>

// libLinal
#include "lvect.h"

class LLKine {
    static const linal::Vect c_ebeam;  // electrons beam direction

 public:
    // Do not instantiate me
    LLKine() = delete;

    // Cosine of polar angle of Lambda in the global frame
    static double cosLambda(const linal::LVect& pr, const linal::LVect& pin);
    // Angles in the Lambda frame
    static std::array<double, 2> omegaLambda(linal::LVect pr, const linal::LVect& pin);
    // Angles in the ant-Lambda frame
    static std::array<double, 5> xi(const linal::LVect& pr, const linal::LVect& pin, const linal::LVect& pbar, const linal::LVect& pip);
};

#endif  // LLKINE_H__
