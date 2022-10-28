import numpy as np

"""
/* COMPILATION of reaction rates for photo-chemistry of hydrogen
   taken from Maselli et al. 2003 (CRASH)
*/
"""

def gammaH0(T):
    res = 5.85e-11
    res *= np.sqrt(T)
    res *= 1. / (1. + np.sqrt(T / 1.e5))
    res *= np.exp(-157809.1 / T)
    return res


def alphaAH(T):
    lambda_ = 2. * 157807. / T
    res = 1.269e-13
    res *= pow(lambda_, 1.503)
    res /= pow(1. + (lambda_ / 0.522) ** 0.47, 1.923)
    return res


def recombinaison_cooling_rates_A_H(T):
    lambda_ = 2. * 157807. / T
    res = 1.778e-29 * pow(lambda_, 1.965)
    res /= pow(1. + pow(lambda_ / 0.541, 0.502), 2.697)
    return res


def alphaBH(T):
    lambda_ = 2. * 157807. / T
    res = 2.753e-14
    res *= pow(lambda_, 1.5)
    res /= pow(1. + (lambda_ / 2.74) ** 0.407, 2.242)
    return res


def betaH(T):
    lambda_ = 2. * 157807. / T
    res = 21.11 * pow(T, -3. / 2.) * np.exp(- lambda_ / 2.) * pow(lambda_, -1.089)
    res /= pow(1. + pow(lambda_ / 0.354, 0.874), 1.01)
    return res


def ksiH0(T):
    res = 1.27e-21 * np.sqrt(T) / (1. + pow(T / 1.e5, 0.5))
    res *= np.exp(-157809.1 / T)
    return res


def etaH0(T):
    res = 8.7e-27 * np.sqrt(T) * pow(T / 1.e3, -0.2) / (1. + pow(T / 1.e6, 0.7))
    return res


def psiH0(T):
    res = 7.5e-19 / (1. + pow(T / 1.e5, 0.5))
    res *= np.exp(-118348. / T)
    return res


def betabremsstrahlung(T):
    res = 1.42e-27 * np.sqrt(T)
    return res


def coolingrate(T, x):
    res = betabremsstrahlung(T) * x ** 2 + psiH0(T) * (1. - x) ** 2 + ksiH0(T) * (1. - x) ** 2 + etaH0(T) * x ** 2
    return res


#
# if(0){
#   // PLOT SOME OF THE COEFFS
#   nT=10000;
#   T=spanl(1.e2,1.e8,nT);
#   ws,1;
#   plh,betaH(T),T,type=2;
#   //  plh,gammaH0(T),T;
#   //  plh,alphaAH(T),T,color="blue";
#   //  plh,alphaBH(T),T,color="red";
#   logxy,1,1;
#   xyleg,"T(K)","cm^3 / s";
#   pltitle,"collisional ionisation rate / recombination A/B rates";
#
#   // is it ok that the alphaB>alphaA above 10^6 ?
#   // shouldnt it always be smaller ?
#
#  };