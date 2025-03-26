import math

def error_sum(devs:list[float], coefficients:list[float]=None):
    """
    Propagates the error to a sum using:
    z = ax + by
    dev^2_z = a^2*dev^2_x + b^2*dev^2_y

    Params:
        devs (list[float]) : the set of standard deviations of the sum terms
        coefficients (list[float]) : the set of coefficients of the sum terms

    Returns:
        dev_sum (float) : the propagated sum error
    """
    if coefficients == None: coefficients = [1] * len(devs)
    return math.sqrt(sum([(c ** 2) * (d ** 2) for c, d in zip(coefficients, devs)]))