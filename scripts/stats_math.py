import math

def average(data : list) -> float :
    """
    Calculates the average of the data set

    Params:
        data (list) : the data set

    Returns:
        average (float) : the calculated average
    """
    return sum(data) / len(data)

def variance(data : list) -> float :
    """
    Calculates the sample variance of the data set (divides by (N - 1))

    Params:
        data (list) : the data set

    Returns:
        variance (float) : the calculated variance
    """
    avg_d = average(data)
    return sum([(d - avg_d) ** 2 for d in data]) / (len(data) - 1)

def standard_deviation(data : list) -> float :
    """
    Calculates the sample standard deviation of the data set (divides by (N - 1))

    Params:
        data (list) : the data set

    Returns:
        standard deviation (float) : the calculated standard deviation
    """
    return math.sqrt(variance(data))

def average_standard_deviation(data : list) -> float :
    """
    Calculates the standard deviation for the average of the data set (divides by (N - 1) and then by √N)

    Params:
        data (list) : the data set

    Returns:
        standard deviation (float) : the calculated standard deviation
    """
    return standard_deviation(data) / math.sqrt(len(data))

def weighted_average(data, weights) -> float:
    """
    Calculates the weighted average for the given data set using the specified weights
    
    Params:
        data (list[tuple]) : the data set where every measure in given in tuples (value, standard_deviation)
        weights (list) : the data set standard deviations

    Returns:
        weighted_average (float) : the calculated weighted average
    """
    products = [w * d for d, w in zip(data, weights)]
    return sum(products) / sum(weights)

def weighted_average_with_standard_deviation(data : list[tuple]) -> tuple[float, float]:
    """
    Calculates the weighted average of a dataset of measures using the measures standard deviations as weights

    Params:
        data (list[tuple]) : the data set where every measure in given in tuples (value, standard_deviation)
        
    Returns:
        (a, d) where a = weighted average and d = weighted average standard deviation
    """

    weights = [1 / (d[1] ** 2) for d in data]
    #ratios = [d[0] / (d[1] ** 2) for d in data]
    ratios = [d[0] * w for d, w in zip(data, weights)]

    w_avg = sum(ratios) / sum(weights)
    w_avg_dev = (1 / sum(weights)) ** 0.5

    return (w_avg, w_avg_dev)