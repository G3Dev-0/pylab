import math

def error_sum(devs:list[float], coefficients:list[float]=None):
    """
    Propagates the error to a sum using:
    z = ax + by
    dev^2_z = a^2 * dev^2_x + b^2 * dev^2_y

    Params:
        devs (list[float]) : the set of standard deviations of the sum terms
        coefficients (list[float]) : the set of coefficients of the sum terms

    Returns:
        dev_sum (float) : the propagated sum error
    """
    if coefficients == None: coefficients = [1] * len(devs)
    return math.sqrt(sum([((c*d) ** 2) for c, d in zip(coefficients, devs)]))

def measure_consistency(m0:tuple[float, float], m1:tuple[float, float]):
    """
    Evaluates the consistency of two measures.
    Formula:
                    |m0 - m1|
        N = -------------------------
            sqrt(dev_m0^2 + dev_m1^2)
    
    Where N is the number of sigmas m0 and m1 are apart from eachother
    
    Params:
        m0 (tuple[float, float]) : the first measure expressed as (value, error)
        m1 (tuple[float, float]) : the second measure expressed as (value, error)

    Returns:
        N (float) : the number of sigmas m0 and m1 are apart from eachother
    """

def chi_2(observed:list[float], expected:list[float]):
    """
    Calculates chi squared (χ²) for the given distributions

    Params:
        observed (list[float]) : the observed distribution
        expected (list[float]) : the expected distribution
    
    Returns:
        chi2 (float) : the calculated value for chi squared (χ²)
    """
    chi2 = 0
    for freq_obs, freq_exp in zip(observed, expected):
        chi2 += ((freq_obs - freq_exp) ** 2) / freq_exp
    return chi2

# TODO: also implement gaussian_chi_2 function for specifically for gaussian distributions

# TODO: implement p-value calculation using 1 - integral