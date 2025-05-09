# PyLab

This program should make the process of doing scientific calculations and writing papers easier.

## DOCUMENTATION

<span id="toc"></span>

### Table of Contents
- [1.0 Calculus](#calc)
- [2.0 Statistics Math](#stats_math)
- [3.0 Error Math](#error_math)
    - [3.1 Measurements Consistency](#measurements_consistency)
    - [3.2 Error Propagation](#error_propagation)
- [4.0 Plot](#plot)
    - [4.1 Plotting](#plotting)
    - [4.2 Graph Customization](#graph_customization)
    - [4.3 Plot Utilities](#plot_utilities)
- [5.0 Linear Regression](#linear_regression)
- [6.0 IO](#io)
- [7.0 JSON](#json)
    - [7.1 Reading and Writing](#reading_and_writing)
    - [7.2 JSON - Python Type Conversion List](#json_python_conversion)
- [8.0 Console](#console)
- [9.0 LaTeX](#latex)
- [10.0 Examples](#examples)
    - [10.1 Plot Examples](#plot_examples)
        - [10.1.1 Plotting a generic function](#plot_examples_generic_function)
        - [10.1.2 Plotting a gaussian distribution](#plot_examples_gaussian_distribution)
    - [10.2 Linear Regression Example](#linear_regression_example)
- [11.0 TO-DO](#todo)
- [12.0 About](#about)

## Quick Picks
Here are some useful links to ofted used commands:

**Linear Regression**
- [Linear Regression](#linear_regression)
- [Linear Regression Example](#linear_regression_example)

**Plot**
- [Histogram](#histogram)
- [Scatter](#scatter)
- [Linked Points](#linked_points)
- [Line](#line)
- [Gaussian](#gaussian)

**Consistency**
- [𝛘²](#chi2)
- [Measure Consistency in 𝜎 (sigma)](#measure_consistency)

<span id="calc"></span>

# 1.0 Calculus [#](#toc)
This module has calculus related functions, namely `derivative` and `integral`.


+ `derivative(f, x0:float, precision:int, round_result:bool=True) -> float`:\
Evaluates the derivative of a given ONE-VARIABLE function f, at a given x0.\
**NOTE:** TOO LOW AND TOO HIGH PRECISION COULD LEAD TO WRONG VALUES.\
\
Evaluates the following:
$$f'(x_0) = \lim_{h \rightarrow 0}{\frac{f(x_0+h) - f(x_0)}{h}}$$

+ `integral(f, a:float, b:float, precision:int, round_result:bool=True) -> float`:\
Evaluates the integral of a given ONE-VARIABLE function from a to b.\
**NOTE:** TOO LOW AND TOO HIGH PRECISION COULD LEAD TO WRONG VALUES.\
**NOTE:** HIGH PRECISION MEANS LONGER CALCULATION TIME.\
\
Evaluates the following:
$$\int_a^b{f(x)dx}$$
<span id="stats_math"></span>

# 2.0 Statistics Math [#](#toc)
This module contains statistics related math functions.

+ `average(data : list) -> float`:\
Calculates the average of the data set.\
\
Evaluates the following:
$$\overline{x} = \frac{\sum_{i=1}^N{x_i}}{N}$$

+ `variance(data : list) -> float`:\
Calculates the sample variance of the data set (divides by (N - 1)).\
\
Evaluates the following:
$$\sigma^2_{x} = \frac{\sum_{i=1}^N{(x_i-\overline{x})^2}}{N-1}$$

+ `standard_deviation(data : list) -> float`:\
Calculates the standard deviation of the data set (divides by (N - 1)).\
\
Evaluates the following:
$$\sigma_{x} = \sqrt{\frac{\sum_{i=1}^N{(x_i-\overline{x})^2}}{N-1}}$$

+ `average_standard_deviation(data : list) -> float`:\
Calculates the standard deviation for the average of the data set (divides by (N - 1) and then by √N).\
\
Evaluates the following:
$$\overline{\sigma_{x}} = \frac{\sigma_{x}}{\sqrt{N}}$$

+ `weighted_average(data, weights) -> float`:\
Calculates the weighted average for the given data set using the specified weights.\
\
Evaluates the following:
$$\mu = \frac{\sum_{i=1}^N{x_i w_i}}{\sum_{i=1}^N{w_i}}$$

+ `weighted_average_with_standard_deviation(data : list[tuple]) -> tuple[float, float]`:\
Calculates the weighted average of a dataset of measures using the measures standard deviations as weights.\
The result is returned as a tuple (weighted_average, weighted_average_standard_deviation).\
\
Evaluates the following:
$$\mu = \frac{\sum_{i=1}^N{x_i w_i}}{\sum_{i=1}^N{w_i}}\quad\text{with}\quad w_i = \frac{1}{\sigma^2_{x_i}}$$

<span id="error_math"></span>

# 3.0 Error Math [#](#toc)
This module contains some fast error propagation functions and some consistency test functions, namely χ² (chi squared) and two-measures consistency.

<span id="measurements_consistency"></span>

## Measurements Consistency [#](#toc)

<span id="measure_consistency"></span>

+ `measure_consistency(m0:tuple[float, float], m1:tuple[float, float])`:\
Returns the consistency $(N)$ of two measures, meaning $N$ is the number of sigmas $a$ and $b$ are apart from eachother.\
\
Evaluates the following:
$$N = \frac{|a-b|}{\sqrt{\sigma_a^2 + \sigma_b^2}}$$

<span id="chi2"></span>

+ `chi_2(observed:list[float], expected:list[float]) -> float`:\
Calculates χ² (chi squared) for the given distributions.\
`observed` is a list containing the observed frequencies ($f_{obs}$);\
`expected` is a list containing the expected frequencies ($f_{exp}$).\
\
Evaluates the following:
$$\chi^2 = \sum_{i=1}^N{\frac{(f_{obs} - f_{exp})^2}{f_{exp}}}$$

<span id="error_propagation"></span>

## Error Propagation [#](#toc)

+ `error_sum(devs:list[float], coefficients:list[float]=None) -> float`:\
Propagates the error for a sum of variables.\
`devs` is the list of standard deviations of the summed variables;\
`coefficients` is the list of the coefficients for the summed variables (leave as `None` to have them be `1`).\
\
Evaluates the following:
$$\sigma_z = \sqrt{a^2\sigma_x^2 + b^2\sigma_y^2}\quad\text{with}\quad z=ax+by$$

<span id="plot"></span>

# 4.0 Plot [#](#toc)
This module is a wrapper for **matplotlib** that makes plotting functions, scattering points and customizing the graph easier.

<span id="plotting"></span>

## 4.1 Plotting [#](#toc)
Here are the functions to plot something to the graph.\

All plotting functions have some specific parameters plus generic ones, namely:
- **z_index**: an integer greater than or equal to 1 that tells matplotlib the layer on which the plot will be drawn.\
*Note*: that you can also set it to 0, but the grid will be drawn on top of the plot.
- **color**: the color of the plot. You can choose it among the ones in the [plot colors list](#plot_colors).
- **alpha** (0-1 float): the alpha channel (transparency) of the plot color.
- **label** (string): the name of the plot (shown on the legend if enabled. See [plot.enable_lengend()](#enable_legend))

<span id="histogram"></span>

+ `hist(data:list, bins:int, normalized:bool, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None)`:\
Plots an histogram with a given number of bins.

<span id="scatter"></span>

+ `scatter(points:list[tuple], y_err=None, hide_scatter:bool=False, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None) -> plt`:\
Plots the given set of points.
You can also specify the width of the vertical error bars with y_err or leave it set a `None` to hide them.\
Setting `hide_scatter=True` makes only the error bars visible.

<span id="linked_points"></span>

+ `linked_points(points:list[tuple], y_err:float=None, z_index:int=1, color:int=DEFAULT_COLOR, alpha:float=1.0, label:str=None) -> plt`:\
Plots a continuous line linking the given set of points.\
This DOES NOT plot the points.\
You can also specify the width of the vertical error bars with y_err or leave it set a `None` to hide them.

<span id="line"></span>

+ `line(slope:float, intercept:float, start:float, end:float, resolution:int, z_index:int=1, color:int=RED_COLOR, alpha:float=1.0, label:str=None)`:\
Plots a line with a given slope, and intercept.\
You can specify from where to `start`, where to `end` and the amount of sample points per unit (`resolution`).

+ `function(f, start:float, end:float, resolution:int, z_index:int=1, color:int=GREEN_COLOR, alpha:float=1.0, label:str=None)`:\
Plots a given one-variable function (`f`).\
You can specify from where to `start`, where to `end` and the amount of sample points per unit (`resolution`).
*Note*: `f` must be a function such as:
```python
def f(x : float) -> float :
    return x + 5
```

<span id="gaussian"></span>

+ `gaussian(mean:float, sigma:float, start:float, end:float, resolution:int, z_index:int=1, color:int=MAGENTA_COLOR, alpha:float=1.0, label:str=None)`:\
Plots a gaussian with a given mean and standard deviation.\
You can specify from where to `start`, where to `end` and the amount of sample points per unit (`resolution`).

<span id="graph_customization"></span>

## 4.2 Graph Customization [#](#toc)

+ `set_title(title)`:\
Sets the graph title to a given string.

+ `set_axis(x_name, y_name)`:\
Sets the x axis name to `x_name` and the y axis name to `y_name`.

<span id="enable_legend"></span>

+ `enable_legend()`:\
Shows the legend in the graph.

+ `enable_grid(horizontal:bool=False, vertical:bool=False)`:\
Shows the horizontal and/or verical grid if enabled.

<span id="plot_utilities"></span>

## 4.3 Plot Utilities [#](#toc)

<span id="plot_colors"></span>
These are the available plot colors:
- DEFAULT_COLOR
- RED_COLOR
- GREEN_COLOR
- BLUE_COLOR
- YELLOW_COLOR
- CYAN_COLOR
- MAGENTA_COLOR
- BLACK_COLOR
- GREY_COLOR

To use them you must refer to them in code as:
`plot.COLOR_NAME`.

+ `separate_coordinates(points:list[tuple[float]]) -> tuple[list[float]]`:\
Returns the coordinates of the points in separate arrays.\
\
For example:
```
points = [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
x, y, z = separate_coordinates(points)
print(f"X: {x}") # [0, 3, 6]
print(f"Y: {y}") # [1, 4, 7]
print(f"Z: {z}") # [2, 5, 8]
```

+ `show()`:\
Shows the graph by opening a matplotlib window.

+ `save(file_name:str, replace_existing:bool=False)`:\
Saves the graph to a "*.png" file with the given file_name.\
The file will be saved to `"./img/file_name.png"`.

+ `clear()`:\
Clears the graph.\
This both removes all the plots and resets all the customizaion options.

<span id="linear_regression"></span>

# 5.0 Linear Regression [#](#toc)
This module contains all that is needed to do linear regression of a set of points.

+ `linear_regression(points:list[tuple[float]], y_err:float=None, fast_plot:bool=False)`:\
Does linear regression on the given set of points.\
You can set `fast_plot = True` to plot the linear fit as well as scattering the points to do a first check.\
The fast plot will be saved to `"./img/fast_linear_regression.png"`.\
\
Returns in the following order:
    - **q**: the calculated line intercept
    - **m**: the calculated line slope
    - **dev_q**: the calculated line intercept standard deviation
    - **dev_m**: the calculated line slope standard deviation
    - **y_err**: the calculated error of the y axis values

<span id="io"></span>

# 6.0 IO [#](#toc)
This module contains some fast txt file reading and writing functions as well as other utility functions.

+ `close(sayGoodbye:bool=True)`:\
Deletes the `"__pycache__"` folder.\
Call this when closing the program.

+ `read(path : str) -> list[str]`:`
Reads the lines of a given file and returns them as a string list.

+ `write(file_name:str, content:str, replace_existing:bool=False)`:\
Writes the content to a `"*.txt"` file with a specific name.\
The file will be saved to `"./txt/{file_name}.txt"`.

<span id="json"></span>

# 7.0 JSON [#](#toc)
This module contains JSON file reading and writing functions.

<span id="reading_and_writing"></span>

## 7.1 Reading and Writing [#](#toc)

+ `load(path:str) -> dict`:\
Reads the content of a given `"*.json"` file and parses it to python types. Returns the content as a **dictionary**.\
See [JSON - Python Type Conversion List](#json_python_conversion).

+ `write(file_name:str, content:dict, replace_existing:bool=False)`:\
Writes the content (given as a **dictionary**) to a `"*.json"` file with a specific name.\
The file will be saved to `"./json/{file_name}.json"`.\
See [JSON - Python Type Conversion List](#json_python_conversion).

<span id="json_python_conversion"></span>

## 7.2 JSON - Python Type Conversion List [#](#toc)

| Python    |    JSON       |
|-----------|---------------|
| dict  	|    Object     |
| list  	|    Array      |
| tuple 	|    Array      |
| str   	|    String     |
| int   	|    Number     |
| float 	|    Number     |
| True  	|    true       |
| False 	|    false      |
| None  	|    null       |

<span id="console"></span>

# 8.0 Console [#](#toc)
This modure contains some print formatting functions and a scientific rounding function.

+ `roundScientific(number:float, significantFigures:int, putDotAfterFirstDigit:bool=False, forceScientificNotation:bool=False) -> str`:\
Rounds a number to a specific amount of significant figures.\
Unless scientific notation use is forced, the algorithm will use it only in the following cases:
    - rounding 321 to 2 significant figures -> 32 * 10 ^ 1
    - rounding 99.9 to 2 significant figures -> 10 * 10 ^ 1

+ `print_measure(measure:tuple[float], unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False) -> str`:\
Creates a format string with the that shows a measurement in a simple way.\
The f-string pattern is the following:\
```python
name="a"
f"{name} = ({value} ± {error}) {unit}"
```

+ `print_measure_list(measurements:list[tuple[float]], units:list[str]=None, names:list[str]=None, separator:str=" ", ending:str="", significant_figures:int=None, force_scientific_notation:bool=False) -> str`:\
Creates a format string with the that shows a set of measurements in a simple way.\
The f-string pattern is the following:\
```python
{name_i} = ({value_i} ± {error_i}){unit_i}{separator}
```
(if all names are given)\
or
```python
{name}_i = ({value_i} ± {error_i}){unit_i}{separator}
```
(if only one name is given it will iterate through by assign a number)\
Ends the string with `{ending}`.\
\
SUPPORTS DIFFERENT UNITS FOR EACH MEASURE

+ `tab(text:str, tabs:int=1) -> str`:
Tabs a text, meaning it adds a customizable number of tabs at the beginning of every line in the given text.

<span id="latex"></span>

# 9.0 LaTeX [#](#toc)
This module is basically a LaTeX formatter and also contains some functions that return often used formulas.

+ `boldText(text) -> str`:\
Returns the bold text written in LaTeX.

+ `italicText(text) -> str`:\
Returns the italic text written in LaTeX.

+ `hyperref(label, text)-> str`:\
Returns an hyperref to a label with replacing text colored in blue and underlined in LaTeX.

+ `overline(expression) -> str`:\
Returns the expression with a line over it written in LaTeX.

+ `vector(expression) -> str`:\
Returns the expression with a vector symbol over it written in LaTeX.

+ `square(expression) -> str`:\
Uses the format: $(\text{expression}) ^ 2$.

+ `cube(expression) -> str`:\
Uses the format: $(\text{expression}) ^ 3$.

+ `power(expression, n) -> str`:\
Uses the format: $(\text{expression}) ^ n$.

+ `sqrt(expression) -> str`:\
Uses the format: $\sqrt{\text{expression}}$.

+ `root(expression, n) -> str`:\
Uses the format: $\sqrt[n]{\text{expression}}$.

+ `number(number:float, unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str`:\
Uses the format:\
```python
{name} = {number} {unit}
```

<span id="measure"></span>

+ `measure(measure:tuple[float], unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str`:\
Uses the format:
```python
{name} = ({measureValue ± measureError}) {unit}
```

+ `measureList(measurements:list[tuple[float]], units:list[str]=None, names:list[str]=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False, separator:str=" ", ending:str="") -> str`:\
Iterates [measure()](#measure) for the whole `measurements` list.

+ `fraction(numerator, denominator) -> str`:\
Uses the format: $\frac{\text{numerator}}{\text{denominator}}$

+ `summation(indexName:str=None, start:int=None, end:str=None, expression:str=None) -> str`:\
Returns the sum expression written in LaTeX.\
Uses the format:
$$\sum_{\text{indexName}=\text{start}}^\text{end}{\text{expression}_{\text{indexName}}}$$

+ `productory(indexName:str=None, start:int=None, end:str=None, expression:str=None) -> str`:\
Returns the product expression written in LaTeX.\
Uses the format:
$$\prod_{\text{indexName}=\text{start}}^\text{end}{\text{expression}_{\text{indexName}}}$$

+ `errorPropagationFormula() -> str`:\
Returns the error propagation formula written in LaTeX, specifically:
$$\sigma_{f} = \sqrt{\sum^N_{i=0}{ \left( \frac{\partial f}{\partial x_i} \sigma_{x_i} \right) ^2}}$$

+ `varianceFormula(xName=None, N:int=None) -> str`:\
Returns the variance formula written in LaTeX, specifically:
$$\sigma^2_{\text{xName}} = \frac{\sum^{N}_{i = 0}{({\text{xName}}_i - \overline{\text{xName}}) ^ 2}}{N - 1}$$

+ `standardDeviationFormula(xName=None, N:int=None) -> str`:\
Returns the standard deviation formula written in LaTeX, specifically:
$$\sigma_{\text{xName}} = \sqrt{\frac{\sum^{N}_{i = 0}{({\text{xName}}_i - \overline{\text{xName}}) ^ 2}}{N - 1}}$$

+ `averageStandardDeviationFormula(xName=None, N:int=None) -> str`:
Returns the average standard deviation formula written in LaTeX, specifically:
$$\sigma_{\overline{\text{xName}}} = \frac{\sigma_{\text{xName}}}{\sqrt{N}}$$

+ `averageFormula(xName=None, N:int=None) -> str`:\
Returns the average formula written in LaTeX, specifically:
$$\overline{\text{xName}}=\frac{1}{N}\sum^{N}_{i=0}{\text{xName}_i}$$

+ `weightedAverageFormula(xName=None, N:int=None) -> str`:\
Returns the weighted average formula written in LaTeX, specifically:
$$\mu_{\text{xName}}=\frac{\sum^{N}_{i=0}{" + x + "_iw_i}}{\sum^{N}_{i=0}{w_i}} \quad\quad\quad w_i=\frac{1}{\sigma^2_i}$$

+ `weightedAverageErrorFormula(xName=None, N:int=None) -> str`:\
Returns the weighted average error formula written in LaTeX, specifically:
$$\sigma_{\mu_{\text{xName}}}=\frac{1}{\sqrt{\sum^{N}_{i=0}{w_i}}} \quad\quad\quad w_i = \frac{1}{\sigma^2_i}$$

<span id="examples"></span>

# 10.0 Examples [#](#toc)
In this section are some examples uses for this library.

<span id="plot_examples"></span>

## 10.1 Plot Examples [#](#toc)
Here are some examples for the **plot** modure uses.

<span id="plot_examples_generic_function"></span>

### 10.1.1 Plotting a generic function [#](#toc)
```python
import scripts.plot as plot

def parabola(x):
    return x ** 2

# plots a red parabola from -8 to 16 with 10 sample points per unit
plot.function(f=parabola, start=-8, end=16, resolution=10, color=plot.RED_COLOR, label="Parabola")
# set the graph title
plot.set_title("The Amazing Parabola")
# set axis names
plot.set_axis(x_name="x", y_name="y")
# only enable the horizontal grid
plot.enable_grid(horizontal=True, vertical=False)
# shows the plot in a matplotlib window
plot.show()
```
The result:
![alt text](/docs/images/parabola_plot.png)

<span id="plot_examples_gaussian_distribution"></span>

### 10.1.2 Plotting a gaussian distribution [#](#toc)
```python
import scripts.plot as plot

# plots a gaussian distribution function from -0.5 to 11 with 10 sample points per unit
plot.gaussian(mean=5.5, sigma=0.02, start=-0.5, end=11, resolution=10, label="Normal Distribution")
# set the graph title
plot.set_title("A Gaussian Distribution")
# set axis names
plot.set_axis(x_name="x", y_name="y")
# only enable the vertical grid
plot.enable_grid(horizontal=False, vertical=True)
# enable the legend
plot.enable_legend()
# saves the plot to "./img/gaussian.png"
plot.save("gaussian")
```
The result:
![alt text](/docs/images/gaussian_plot.png)

<span id="linear_regression_example"></span>

## 10.2 Linear Regression Example [#](#toc)
```python
import scripts.linear_regression as lr
import scripts.plot as plot

volume_pressure = [
    (25.9, 1014.5),
    (35.0, 1043.2),
    (45.0, 1076.2),
    (55.0, 1109.2),
    (64.8, 1142.3),
    (74.8, 1172.6)
]

# FAST PLOT
# apply the linear regression and also do a fast plot
q, m, dev_q, dev_m, dev_y = lr.linear_regression(volume_pressure, fast_plot=True)

# CUSTOM PLOT
# plot the calculated data on a well refined graph

# get the x coordinates of the points (volume values)
x_values, _ = plot.separate_coordinates(volume_pressure)
# find the minimum volume value
min_x = min(x_values)
# find the maximum volume value
max_x = max(x_values)
# plot the calculated line
plot.line(m, q, min_x, max_x, 10, color=plot.GREEN_COLOR, label="Linear Fit")
# scatter the points with the calculated error bars
plot.scatter(volume_pressure, y_err=dev_y, color=plot.RED_COLOR, label="Volume-Pressure")
# customize the plot
plot.set_title("Linear Fit")
plot.set_axis(x_name="Volume [mL]", y_name="Pressure [hPa]")
plot.enable_grid(horizontal=True, vertical=True)
plot.enable_legend()
# save the plot to "./img/linear_fit.png"
plot.save("linear_fit")
```
The results:
#### Linear Regression: Fast Plot
![alt text](/docs/images/fast_linear_regression.png)

#### Linear Regression: Customized Plot
![alt text](/docs/images/linear_fit.png)

<span id="todo"></span>

# 11.0 TO-DO [#](#toc)
To do list:
+ implement a p-value calculation function
+ implement poisson plot function
+ improve and add error propagation
+ use LaTeX equations to explain the applied formulas in the functions

<span id="about"></span>

# 12.0 About [#](#toc)
Made by [**G3Dev**](https://github.com/G3Dev-0), 2025\
Used Technologies: [**matplotlib**](https://matplotlib.org/)
Version: [**v1.1 b08052025-0**](https://github.com/G3Dev-0/pylab)
