import scripts.io as io

import matplotlib.pyplot as plt
import numpy as np

# COLORS
DEFAULT_COLOR = "#1F77B4"
RED_COLOR = "red"
GREEN_COLOR = "green"
BLUE_COLOR = "blue"
YELLOW_COLOR = "yellow"
CYAN_COLOR = "cyan"
MAGENTA_COLOR = "magenta"
BLACK_COLOR = "black"
GREY_COLOR = "grey"
LIME_COLOR = "lime"
ORANGE_COLOR = "orange"
SALMON_COLOR = "salmon"
CORNFLOWER_BLUE_COLOR = "cornflowerblue"

# MARKERS
INVISIBLE_MARKER = "none"
POINT_MARKER_MARKER = "."
CIRCLE_MARKER = "o"
TRIANGLE_DOWN_MARKER = "v"
TRIANGLE_UP_MARKER = "^"
TRIANGLE_LEFT_MARKER = "<"
TRIANGLE_RIGHT_MARKER = ">"
OCTAGON_MARKER = "8"
SQUARE_MARKER = "s"
PENTAGON_MARKER = "p"
PLUS_FILLED_MARKER = "P"
STAR_MARKER = "*"
HEXAGON_1_MARKER = "h"
HEXAGON_2_MARKER = "H"
PLUS_MARKER = "+"
CROSS_MARKER = "x"
CROSS_FILLED_MARKER = "X"
DIAMOND_MARKER = "D"
THIN_DIAMOND_MARKER = "d"
HORIZONTAL_LINE_MARKER = "_"

# LINE STYLES
INVISIBLE_LINE = ""
CONTINUOUS_LINE = "-"
DASHED_LINE = "--"
DOTTED_LINE = ":"
DASH_DOT_LINE = "-."

def separate_coordinates(points:list[tuple[float]], coordinate_to_return:int=None) -> tuple[list[float]]:
    """
    Returns the coordinates of the points in separate arrays

    Params:
        points (list[tuple[float]]) : an array of N-dimensional points
        coordinate_to_return (int) : the index of the coordinate to return (0 is the first, 1 is the second and so on) (if set to None all coordinates are returned)
    
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
    if coordinate_to_return == None: return tuple(coordinates)
    else: return tuple(coordinates)[coordinate_to_return]

def get_range(points:list[tuple[float]], coordinate_to_use:int):
    """
    Returns the range the array of points spans on considering the given coordinate_to_use.
    e.g.: if coordinate_to_use is 0 (x) the method will return the minimum x and the maximum x
    
    Params:
        points (list[tuple[float]]) : the list of points
        coorinate_to_use (int) : the index of the coordinate to use (0 = x, 1 = y, 2 = z, 3 = w, ...)
    Returs:
        range (tuple[float, float]) : the range the points span on (min, max)
    """
    vals = separate_coordinates(points)[coordinate_to_use]
    min_val = min(vals)
    max_val = max(vals)
    return (min_val, max_val)

def show():
    """
    Shows the graph
    """
    plt.show()

def save(file_name:str, replace_existing:bool=False):
    """
    Saves the graph to a "*.png" file with a specific name.\\
    The file will be saved to "./img/{file_name}.png"

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

def hist(
        # plot data
        data:list, bins:int, normalized:bool,
        
        # color
        color:str=DEFAULT_COLOR,
        
        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None):
    plt.hist(data, bins=bins, density=normalized, zorder=z_index, color=color, alpha=alpha, label=label)

def scatter(
        # plot data
        points:list[tuple],
        x_err=None,
        y_err=None,
        
        # styles
        marker:str=CIRCLE_MARKER,
        line_style:str=INVISIBLE_LINE,

        # colors
        color:str=DEFAULT_COLOR,
        border_color:str=None,
        errorbar_color:str=None,
        line_color:str=GREY_COLOR,
        
        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None) -> plt :
    """
    Plots the given set of points.\\
    You can also specify the height of the vertical error bars with y_err\\
    and the label shown in the legend.\\
    You can set the z index and the color.

    Params:
        points (list[tuple(float)]) : the set of points to be plotted
        x_err : the x error bar value
        y_err : the y error bar value
        
        marker (str) : the marker of the plot (use the plot.MARKER_NAME constants) (plot.INVISIBLE_MARKER hides the points)
        line_style (str) : the style of the linking line (use the plot.LINE_STYLE constants) (plot.INVISIBLE_LINE hides the line)
        
        color (str) : the color of the scattered points (use the plot.COLOR_NAME constants)
        border_color (str) : the border color of the scattered points (use the plot.COLOR_NAME constants) (if set to "None" it will be equal to color)
        errorbar_color (str) : the color of the points error bars (use the plot.COLOR_NAME constants) (if set to "None" it will be equal to color)
        line_color (str) : the color of the line linking the points (use the plot.COLOR_NAME constants)
        
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    x_val, y_val = [point[0] for point in points], [point[1] for point in points]

    if border_color == None: border_color = color
    if errorbar_color == None: errorbar_color = color

    plt.errorbar(x_val, y_val, xerr=x_err,yerr=y_err,       # x, y, x_error, y_error
                fmt=f'{marker}{line_style}',                # marker and line style
                color=line_color,                           # line color
                ecolor=errorbar_color,                      # error bars color
                markerfacecolor=color,                      # marker color
                markeredgecolor=border_color,               # marker border color
                capsize=6,                                  # error bar width
                zorder=z_index,
                alpha=alpha,
                label=label)
    
    return plt

def errorbar_points(
        # plot data
        points:list[tuple],
        x_err=None,
        y_err=None,
        
        # styles
        marker:str=CIRCLE_MARKER,

        # colors
        color:str=DEFAULT_COLOR,
        border_color:str=None,
        errorbar_color:str=None,
        
        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None) -> plt :
    """
    Plots the given set of points with error bars and no linking line by default.\\
    You can also specify the height of the vertical error bars with y_err\\
    and the label shown in the legend.\\
    You can set the z index and the color.

    Params:
        points (list[tuple(float)]) : the set of points to be plotted
        y_err : the set of points to be plotted
        
        marker (str) : the marker of the plot (use the plot.MARKER_NAME constants) (plot.INVISIBLE_MARKER hides the points)
        
        color (str) : the color of the scattered points (use the plot.COLOR_NAME constants)
        border_color (str) : the border color of the scattered points (use the plot.COLOR_NAME constants) (if set to "None" it will be equal to color)
        errorbar_color (str) : the color of the points error bars (use the plot.COLOR_NAME constants) (if set to "None" it will be equal to color)
        
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    return scatter(
        points,
        x_err,
        y_err,
        
        marker,
        INVISIBLE_LINE,
        
        color,
        border_color,
        errorbar_color,
        None,
        
        z_index,
        alpha,
        label)

def linked_points(
        # plot data
        points:list[tuple],
        
        # styles
        marker:str=CIRCLE_MARKER,
        line_style:str=CONTINUOUS_LINE,

        # colors
        color:str=DEFAULT_COLOR,
        border_color:str=None,
        line_color:str=GREY_COLOR,
        
        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None) -> plt :
    """
    Plots the given set of points with a linking line connecting them and no error bars by default.\\
    You can also set the label shown in the legend.\\
    You can set the z index and the color.

    Params:
        points (list[tuple(float)]) : the set of points to be plotted
        
        marker (str) : the marker of the plot (use the plot.MARKER_NAME constants) (plot.INVISIBLE_MARKER hides the points)
        line_style (str) : the style of the linking line (use the plot.LINE_STYLE constants) (plot.INVISIBLE_LINE hides the line)
        
        color (str) : the color of the scattered points (use the plot.COLOR_NAME constants)
        border_color (str) : the border color of the scattered points (use the plot.COLOR_NAME constants) (if set to "None" it will be equal to color)
        line_color (str) : the color of the line linking the points (use the plot.COLOR_NAME constants)
        
        z_index (int) : the plot z index (0 (minimum) = grid lines) (higher z index means being drawn over plots with lower z index)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    return scatter(
        points,
        None,
        None,
        
        marker,
        line_style,
        
        color,
        border_color,
        None,
        line_color,
        
        z_index,
        alpha,
        label)

def line(
        # plot data
        slope:float,
        intercept:float,

        # function specific data
        start:float,
        end:float,
        resolution:int,
        
        # color
        color:str=RED_COLOR,
        
        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None):
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
        color (str) : the color of the plot (use the plot.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    xs = np.linspace(start, end, int(resolution * (end - start)))
    ys = intercept + xs * slope

    plt.plot(xs, ys, zorder=z_index, color=color, alpha=alpha, label=label)

    return plt

def function(
        # plot data
        f,
        
        # functions specific data
        start:float,
        end:float,
        resolution:int,
        
        # color
        color:str=GREEN_COLOR,

        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None):
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
        color (str) : the color of the plot (use the plot.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    xs = np.linspace(start, end, int(resolution * (end - start)))
    ys = f(xs)

    plt.plot(xs, ys, zorder=z_index, color=color, alpha=alpha, label=label)

    return plt

def gaussian(
        # plot data
        mean:float,
        sigma:float,
        
        # function specific data
        start:float,
        end:float,
        resolution:int,
        
        # color
        color:str=MAGENTA_COLOR,

        # others
        z_index:int=2,
        alpha:float=1.0,
        label:str=None):
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
        color (str) : the color of the plot (use the plot.COLOR_NAME constants)
        alpha (float) : the color alpha channel (transparency)
        label (str) : the label that will be shown in the legend for this plot
    """
    def norm(x):
        return np.exp(-0.5 * (((x - mean) / (sigma)) ** 2)) / (sigma * np.sqrt(2 * np.pi))
    return function(norm, start, end, resolution, z_index, color, alpha, label)