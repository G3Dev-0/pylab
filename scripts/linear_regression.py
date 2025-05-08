from scripts import plot

import math

def linear_regression(points:list[tuple[float]], y_err:float=None, fast_plot:bool=False):
    """
    Does linear regression on the given set of points.\\
    You can set fast_plot to True to plot the linear fit as well as scattering the points to do a first check.
    The fast plot will be saved to "./img/fast_linear_regression.png"
    

    Params:
        points (list[tuple[float]]) : the set of points
        dev_y (float) : the standard deviation for the y values
        fast_plot (bool) : plots the linear fit if set to true (useful for a first check)

    Returns:
        q (float) : the calculated line intercept
        m (float) : the calculated line slope
        dev_q (float) : the calculated line intercept standard deviation
        dev_m (float) : the calculated line slope standard deviation
        y_err_post (float) : the calculated error of the y axis values
    """

    # N è il numero di punti
    N = len(points)
    # i valori in x sono le ascisse dei punti dati
    x_values = [point[0] for point in points]
    # i valori in y sono le ordinate dei punti dati
    y_values = [point[1] for point in points]
    # calcola l'incertezza dei valori in y = media delle diverse incertezze dei valori in y
    dev_y = y_err#sum([point[2] for point in points]) / N

    # valori utili per calcolare q, m, dev_q e dev_m
    x = sum(x_values)
    y = sum(y_values)
    x_2 = sum([x_value ** 2 for x_value in x_values])
    x_y = sum([x_value * y_value for x_value, y_value in zip(x_values, y_values)])
    delta = (N * x_2) - (x ** 2)
    
    # calcola intercetta e coefficiente angolare
    q = (1 / delta) * ((x_2 * y) - (x * x_y))
    m = (1 / delta) * ((N * x_y) - (x * y))
    
    # calcola incertezza di y a posteriori
    y_err_post = math.sqrt(sum([(q + (m*x) - y)**2 for x, y in zip(x_values, y_values)]) / (N - 2))

    # usala per calcolare dev_m e dev_q
    if dev_y == None: dev_y = y_err_post

    # calcola le incertezze dell'intercetta e del coefficiente angolare
    dev_q = dev_y * math.sqrt((x ** 2) / delta)
    dev_m = dev_y * math.sqrt(N / delta)

    if fast_plot:
        xx, _ = plot.separate_coordinates(points)
        min_x, max_x = min(xx), max(xx)
        plot.line(m, q, min_x, max_x, 10, label="Linear Fit")
        plot.scatter(points, y_err=dev_y, label="Points")
        plot.set_title("Fast Linear Regression")
        plot.enable_grid(True, True)
        plot.enable_legend()
        plot.set_axis("x", "y")
        plot.save("fast_linear_regression", True)
        plot.clear()
    
    return q, m, dev_q, dev_m, dev_y