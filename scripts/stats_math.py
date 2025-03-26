import math

def avg(data : list) -> float :
    """
    Calculates the average of the data set

    Params:
        data (list) : the data set

    Returns:
        average (float) : the calculated average
    """
    return sum(data) / len(data)

def var(data : list) -> float :
    """
    Calculates the variance of the data set (divides by (N - 1))

    Params:
        data (list) : the data set

    Returns:
        variance (float) : the calculated variance
    """
    avg_d = avg(data)
    return sum([(d - avg_d) ** 2 for d in data]) / (len(data) - 1)

def dev(data : list) -> float :
    """
    Calculates the standard deviation of the data set (divides by (N - 1))

    Params:
        data (list) : the data set

    Returns:
        standard deviation (float) : the calculated standard deviation
    """
    return math.sqrt(var(data))

def dev_avg(data : list) -> float :
    """
    Calculates the standard deviation for the average of the data set (divides by (N - 1) and then by √N)

    Params:
        data (list) : the data set

    Returns:
        standard deviation (float) : the calculated standard deviation
    """
    return dev(data) / math.sqrt(len(data))