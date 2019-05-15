#include "fitter.h"

#include "Minuit2/MnMigrad.h"

using namespace ROOT::Minuit2;
using namespace llfit;

// 0.6, 0.5*3.1415, 0.6, -0.6
Fitter::Fitter(TheFCN& fcn) : m_fcn(fcn) {
    m_upar.Add("alpha", 0.6, 0.1, -1., 1.);
    m_upar.Add("dPhi", 1.55, 0.1, -3.1415, 3.1415);
    m_upar.Add("alpha1", 0.6, 0.1, -1., 1.);
    m_upar.Add("alpha2", -0.6, 0.1, -1., 1.);
    m_upar.Add("xi", 0.8, 0.1, -1.05, 1.05);
}

FunctionMinimum Fitter::fit() {
    MnMigrad migrad(m_fcn, m_upar);
    return migrad();
}
