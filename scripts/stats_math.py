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

def weighted_avg(data, weights) -> float:
    products = [w * d for d, w in zip(data, weights)]
    return sum(products) / sum(weights)

def weighted_avg_with_dev(data : list[tuple]) -> tuple[float, float]:
    """
    Calculates the weighted average of a dataset of measures with standard deviations

    Params:
        data (list[tuple]) : the data set where every measure in given in tuples (value, standard_deviation)
        devs (list) : the data set standard deviations
        
    Returns:
        (a, d) where a = weighted average and d = weighted average standard deviation
    """

    weights = [1 / (d[1] ** 2) for d in data]
    ratios = [d[0] / (d[1] ** 2) for d in data]

    w_avg = sum(ratios) / sum(weights)
    w_avg_dev = (1 / sum(weights)) ** 0.5

    return (w_avg, w_avg_dev)