from scripts import io

import matplotlib.pyplot as plt
import numpy as np

COLORS = ["#1F77B4", "red", "green", "blue", "yellow", "cyan", "magenta", "black", "grey"]
DEFAULT_COLOR = 0
RED_COLOR = 1
GREEN_COLOR = 2
BLUE_COLOR = 3
YELLOW_COLOR = 4
CYAN_COLOR = 5
MAGENTA_COLOR = 6
BLACK_COLOR = 7
GREY_COLOR = 8

def separate_coordinates(points:list[tuple[float]]) -> tuple[list[float]]:
    """
    Returns the coordinates of the points in separate arrays

    Params:
        points (list[tuple[float]]) : an array of N-dimensional points
    
    Returns:
        coordinates (tuple[list[float]]) : a tuple of N entries each one being an array of the coordinates of the points
    """
    n = None
    for point in points:
        if n == None: n = len(point)
        elif n != len(point):
            print("[Error]: Not all the points have the same number of coordinates")
            return
    coordinates = [[] for _ in range(n)]
    for i, point in enumerate(points):
        for j in range(n):
            coordinates:tuple[list[float]]
            coordinates[j].append(points[i][j])
    return tuple(coordinates)

def show():
    """
    Shows the graph
    """
    plt.show()

def save(file_name:str, replace_existing:bool=False):
    """
    Saves the graph to a "*.png" file with a specific name.\\
    The file will be saved to "./img/file_name.png"

    Params:
        file_name (str) : the file name
        replace_existng (bool) : if set to True it automatically replaces an already existing file (if there is any), otherwise it asks the user to confirm before proceding
    """
    path = f"{io.IMG_PATH}/{file_name}.png"
    if io.check_for_dir_file_to_save(path, io.IMG_PATH, replace_existing):
        plt.savefig(path)

    """if not os.path.exists(IMG_PATH): os.mkdir(IMG_PATH)
    if os.path.exists(path) and not replace_existing:
        if input(f"Another file with the same name already exists at '{path}'. Do you want to replace it? [ENTER/n]") == "n":
            return
    plt.savefig(path)"""

def clear():
    """
    Clears the plot by closing it
    """
    plt.close()

def set_title(title):
    """
    Sets the graph title to a given string

    Params:
        title (str) : the graph title
    """
    plt.title(title)

def set_axis(x_name, y_name):
    """
    Sets the axis names to two given strings

    Params:
        x_name (str) : the x axis name
        y_name (str) : the y axis name
    """
    plt.xlabel(x_name)
    plt.ylabel(y_name)

def enable_legend():
    """
    Shows the legend in the graph
    """
    plt.legend(title="Legenda")

def enable_grid(horizontal:bool=False, vertical:bool=False):
    """
    Shows the horizontal and/or verical grid if enabled
    """
    visible = horizontal or vertical
    axis = ""
    if horizontal and vertical: axis = "both"
    elif horizontal: axis = "x"
    elif vertical: axis = "y"
    plt.grid(visible=visible, axis=axis, zorder=0)

def hist(data:list, bins:int, normalized:bool, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None):
    plt.hist(data, bins=bins, density=normalized, zorder=z_index, color=COLORS[color], alpha=alpha, label=label)

def scatter(points:list[tuple], y_err=None, hide_scatter:bool=False, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None) -> plt :
    """
    Plots the given set of points.\\
    You can also specify the width of the vertical error bars with y_err\\
    and the label shown in the legend.\\
    You can set the z index and the color.

    Params:
        points (list[tuple(float)]) : the set of points to be plotted
        y_err (float) : the set of points to be plotted
        hide_scatter (bool) : hides the points if set to True, shows them otherwise
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        color (int) : the color of the plot (use the plot_utils.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    x_val, y_val = [point[0] for point in points], [point[1] for point in points]
    if y_err == None:
        plt.scatter(x_val, y_val, zorder=z_index, color=COLORS[color], alpha=alpha, label=label)
    else:
        errors = y_err
        if type(y_err) == float: errors = [y_err]*len(points)
        style = "none" if hide_scatter else "o"
        plt.errorbar(x_val, y_val, yerr=errors, fmt=style, capsize=6, zorder=z_index, alpha=alpha, color=COLORS[color], label=label)
    return plt

def linked_points(points:list[tuple], y_err:float=None, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None) -> plt :
    """
    Plots a continuous line linking the given set of points.\\
    You can also specify the width of the vertical error bars with y_err\\
    and the label shown in the legend.\\
    You can set the z index and the color.

    Params:
        points (list[tuple(float)]) : the set of points to be plotted
        y_err (float) : the set of points to be plotted
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        color (int) : the color of the plot (use the plot_utils.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    x_val, y_val = [point[0] for point in points], [point[1] for point in points]
    plt.plot(x_val, y_val, zorder=z_index, color=COLORS[color], alpha=alpha, label=label)
    if y_err != None:
        plt.errorbar(x_val, y_val, yerr=[y_err]*len(points), fmt="o", capsize=4, alpha=alpha)
    return plt

def line(slope:float, intercept:float, start:float, end:float, resolution:int, z_index:int=1, color:int=RED_COLOR, alpha:float=1.0, label:str=None):
    """
    Plots a line with a given slope, and intercept.\\
    You can specify from where to start, where to end and the amount of sample points (resolution) per unit.\\
    You can also give a label that will be displayed in the legend for this plot.\\
    You can set the z index and the color.

    Params:
        slope (float) : the line slope
        intercept (float) : the line intercept
        start (float) : the x position where the line begins
        end (float) : the x position where the line ends
        resolution (int) : the amount of sample points per unit
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        color (int) : the color of the plot (use the plot_utils.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    xs = np.linspace(start, end, int(resolution * (end - start)))
    ys = intercept + xs * slope

    plt.plot(xs, ys, zorder=z_index, color=COLORS[color], alpha=alpha, label=label)

    return plt

def function(f, start:float, end:float, resolution:int, z_index:int=1, color:int=GREEN_COLOR, alpha:float=1.0, label:str=None):
    """
    Plots a given function.\\
    You can specify from where to start, where to end and the amount of sample points (resolution) per unit.\\
    You can also give a label that will be displayed in the legend for this plot.\\
    You can set the z index and the color.

    Params:
        f (function) : the function to plot. IT MUST TAKE A SINGLE FLOAT PARAMETER AND A RETURN A SINGLE FLOAT
        start (float) : the x position where the line begins
        end (float) : the x position where the line ends
        resolution (int) : the amount of sample points per unit
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        color (int) : the color of the plot (use the plot_utils.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    xs = np.linspace(start, end, int(resolution * (end - start)))
    ys = f(xs)

    plt.plot(xs, ys, zorder=z_index, color=COLORS[color], alpha=alpha, label=label)

    return plt

def gaussian(mean:float, sigma:float, start:float, end:float, resolution:int, z_index:int=1, color:int=MAGENTA_COLOR, alpha:float=1.0, label:str=None):
    """
    Plots a gaussian with a given mean and standard deviation.\\
    You can specify from where to start, where to end and the amount of sample points (resolution) per unit.\\
    You can also give a label that will be displayed in the legend for this plot.\\
    You can set the z index and the color.

    Params:
        mean (float) : the mean where the gaussian will be centered
        sigma (float) : the standard deviation that will define the gaussian
        start (float) : the x position where the line begins
        end (float) : the x position where the line ends
        resolution (int) : the amount of sample points per unit
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        color (int) : the color of the plot (use the plot_utils.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    def norm(x):
        return np.exp(-0.5 * (((x - mean) / (sigma)) ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return function(norm, start, end, resolution, z_index, color, alpha, label)