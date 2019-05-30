/** Unbinned maximum likelihood fit for Lambda formfactors and electron beam polarization **/

#ifndef FITTER_H_HH
#define FITTER_H_HH

#include "Minuit2/MnUserParameters.h"
#include "Minuit2/FunctionMinimum.h"
#include "Minuit2/MnPrint.h"

#include "fcn.h"

namespace llfit {

class Fitter {
    TheFCN& m_fcn;
    ROOT::Minuit2::MnUserParameters m_upar;

 public:
    Fitter(TheFCN& fcn);
    ROOT::Minuit2::FunctionMinimum fit();
};

}

#endif  // FITTER_H_HH
