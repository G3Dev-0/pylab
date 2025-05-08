def derivative(f, x0:float, precision:int, round_result:bool=True) -> float:
    """
    Evaluates the derivative of a given ONE-VARIABLE function at a given x0.
    NOTE: TOO LOW AND TOO HIGH PRECISION COULD LEAD TO WRONG VALUES

    Params:
        f (function) : the function to derive
        x0 (float) : the x position at which the derivative will be calculated
        precision (int) : the precision of the derivative calculation
        round_result (bool) : rounds the result to 3 decimal digits if set to True

    Returns:
        derivative (float) : the evaluated derivative
    """
    h = 10 ** -precision
    deri = (f(x0 + h) - f(x0)) / h
    if round_result: deri = round(deri, ndigits=3)
    return deri

def integral(f, a:float, b:float, precision:int, round_result:bool=True) -> float:
    """
    Evaluates the integral of a given ONE-VARIABLE function from a to b.
    NOTE: TOO LOW AND TOO HIGH PRECISION COULD LEAD TO WRONG VALUES
    NOTE: HIGH PRECISION MEANS LONGER CALCULATION TIME

    Params:
        f (function) : the function to integrate
        a (float) : the left integration limit
        b (float) : the right integration limit
        precision (int) : the precision of the integral calculation
        round_result (bool) : rounds the result to 3 decimal digits if set to True

    Returns:
        integral (float) : the evaluated integral
    """
    dx = 10 ** -precision
    inte = 0
    x = a
    counter = 0
    while x < b:
        counter += 1
        inte += f(x) * dx
        x += dx
        
    inte += f(b) * dx
    if round_result: inte = round_result(inte, ndigits=3)
    return inte