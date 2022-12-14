import numpy as np
import scipy.constants as sc

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
    res = 21.11 * pow(T, -3. / 2.) * np.exp(-lambda_ / 2.) * pow(lambda_, -1.089)
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


def cooling_rate(T, x):
    res = betabremsstrahlung(T) * x ** 2 + psiH0(T) * (1. - x) ** 2 + ksiH0(T) * (1. - x) ** 2 + etaH0(T) * x ** 2
    return res


def Q_root(T, Ngamma, ro, x, dt):
    sigma = 1.63e-18
    m = (alphaBH(T) + betaH(T)) * ro ** 2 * dt
    n = ro - (alphaAH(T) + betaH(T)) * ro / (sigma * sc.c * 1e2) - alphaBH(T) * ro ** 2 * dt - 2 * betaH(
        T) * ro ** 2 * dt
    p = -ro * (1 + x) - Ngamma - 1 / (sigma * sc.c * 1e2 * dt) + betaH(T) * ro / (sigma * sc.c * 1e2) + betaH(
        T) * ro ** 2 * dt
    q = Ngamma + ro * x + x / (sigma * sc.c * 1e2 * dt)
    coef = [m, n, p, q]
    res = np.roots(coef)
    for i in res:
        if 1 > i > 0:
            return i
    return res


# updt_Ngamma (p+1) = N_gamma' + ?? * ro**2 * (1 - X) * X * dt - alphaB * ro**2 * X**2 * dt - ro * (X - x) cf (A5)
def updt_Ngamma(T, Ngamma, ro, x, dt):
    res = Ngamma + betaH(T) * ro ** 2 * (1 - Q_root(T, Ngamma, ro, x, dt)) * Q_root(T, Ngamma, ro, x,
                                                                                    dt) * dt - alphaBH(
        T) * ro ** 2 * Q_root(T, Ngamma, ro, x, dt) ** 2 * dt - ro * (Q_root(T, Ngamma, ro, x, dt) - x)
    return res
