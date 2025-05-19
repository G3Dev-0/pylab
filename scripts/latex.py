from scripts import console as cu

def boldText(text) -> str:
    """
    Returns the bold text written in LaTeX
    """
    return "\\textbf{" + f"{text}" + "}"

def italicText(text) -> str:
    """
    Returns the italic text written in LaTeX
    """
    return "\\textit{" + f"{text}" + "}"

def hyperref(label, text):
    """
    Returns an hyperref to a label with replacing text colored in blue and underlined in LaTeX
    """
    return "\\hyperref[" + label + "]{\\color{blue}\\underline{" + text + "}\\color{black}}"

def overline(expression) -> str:
    """
    Returns the expression with a line over it written in LaTeX
    """
    return "\\overline{" + f"{expression}" + "}"

def vector(expression) -> str:
    """
    Returns the expression with a vector symbol over it written in LaTeX
    """
    return "\\vec{" + f"{expression}" + "}"

def square(expression) -> str:
    """
    Uses the format: ({expression}) ^ 2

    Params:
        expression (any) : the expression to put under a square symbol

    Returns:
        latex (str) : the squared expression between parenthesis written in LaTeX
    """
    return f"({expression}) ^ 2"

def cube(expression) -> str:
    """
    Uses the format: ({expression}) ^ 3

    Params:
        expression (any) : the expression to put under a cube symbol

    Returns:
        latex (str) : the cubed expression between parenthesis written in LaTeX
    """
    return f"({expression}) ^ 3"

def power(expression, n) -> str:
    """
    Uses the format: ({expression}) ^ n
    
    Params:
        expression (any) : the expression to put under a power symbol
        n (int) : the power

    Returns:
        latex (str) : the expression to the power of n between parenthesis written in LaTeX
    """
    return f"({expression}) ^ {n}"

def sqrt(expression) -> str:
    """
    Uses the format: √ ({expression})

    Params:
        expression (any) : the expression to put under a square root symbol

    Returns:
        latex (str) : the expression under a square root symbol written in LaTeX
    """
    return "\\sqrt{" + f"{expression}" + "}"

def root(expression, n) -> str:
    """
    Uses the format: n √ ({expression})

    Params:
        expression (any) : the expression to put under a root symbol
        n (int) : the root index

    Returns:
        latex (str) : the expression under a n-th root symbol written in LaTeX
    """
    return "\\sqrt[" + f"{n}" + "]{" + f"{expression}" + "}"

def number(number:float, unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str:
    """
    Uses the format: $ (or $$){name} = {number} {unit}$ (or $$)

    Params:
        number (float) : the number to write in LaTeX
        unit (str) : the number unit
        name (str) : the number name
        significantFigures (int) : the number of significantFigures the number will be rounded to
        forceScientificNotation (bool) : if set to True it forces the rounding algorithm to use scientific notation where possible
        centered (bool) : if set to True it makes the number latex equation string centered

    Returns:
        latex (str) : the number written in LaTeX
    """
    delimiter = "$$" if centered else "$"
    nameStr = f'{name} = ' if name != None else ''
    numberStr = cu.roundScientific(number, significant_figures, False, force_scientific_notation)
    unitStr = unit if unit != None else ''
    return f"{delimiter}{nameStr}{numberStr}{unitStr}{delimiter}"

def measure(measure:tuple[float], unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str:
    """
    Uses the format: $ (or $$){name} = ({measureValue ± measureError}) {unit}$ (or $$)

    Params:
        measure (list[tuple[float]]) : the measure list
        unit (str) : the measure unit
        name (str) : the measure name
        significantFigures (int) : the number of significantFigures the numbers will be rounded to
        forceScientificNotation (bool) : if set to True it forces the rounding algorithm to use scientific notation where possible
        centered (bool) : if set to True it makes the latex equation string centered

    Returns:
        latex (str) : the measure written in LaTeX
    """
    delimiter = "$$" if centered else "$"
    
    if name == None: name = ""
    else: name += " = "

    if unit == None: unit = ""

    value = measure[0]
    error = measure[1]
    
    if significant_figures != None: value = cu.roundScientific(value, significant_figures, False, force_scientific_notation)
    if significant_figures != None: error = cu.roundScientific(error, significant_figures, False, force_scientific_notation)

    measureStr = f"{name}({value} \\pm {error})\\text" + "{" +  f" {unit}" + "}"

    return f"{delimiter}{measureStr}{delimiter}"

def measureList(measurements:list[tuple[float]], units:list[str]=None, names:list[str]=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False, separator:str=" ", ending:str="") -> str:
    """
    Params:
        measurements (list[tuple[float]]) : the measure list
        units (list[str]) : the measurements units (you can put just one element and it will be repeated)
        names (list[str]) : the measurements names (you can put just one element and it will be repeated with an "_i" at the end)
        significantFigures (int) : the number of significantFigures the numbers will be rounded to
        forceScientificNotation (bool) : if set to True it forces the rounding algorithm to use scientific notation where possible
        centered (bool) : if set to True it makes the whole set of latex equation strings centered
        separator (str) : a char sequence that separates the measures
        ending (str) : a char sequence to end the string with

    Returns:
        latex (str) : the measure list written in LaTeX
    """

    if units == None: units = [""] * len(measurements)
    if len(units) == 1: units = [units[0]] * len(measurements)

    if names == None: names = [None] * len(measurements)
    if len(names) == 1: names = [names[0]] * len(measurements)

    latex = ""
    
    i = 0
    for m in measurements:
        formattedMeasure = measure(m, units[i], names[i], significant_figures, force_scientific_notation, centered)
        latex += f"{formattedMeasure}{separator}"
        i += 1
    
    return f"{latex.removesuffix(separator)}{ending}"

def equation(expression, bold:bool=False, centered:bool=False, equationNumber=None) -> str: #, delimiterOn:bool=True):
    """
    Params:
        expression (any) : the equation expression
        bold (bool) : if set to True it makes the whole equation bold
        centered (bool) : if set to True it makes the whole equation centered
        equationNumber (int) : a number that gets added after the equation in the format (N)

    Returns:
        latex (str) : the equation written in LaTeX
    """
    if bold: expression = "\\boldsymbol{" + f"{expression}" + "}"
    delimiter = "$$" if centered else "$"
    #if not delimiterOn: delimiter = ""
    equationNumberStr = "\\tag{" + str(equationNumber) + "}" if equationNumber != None else ""
    return f"{delimiter}{expression}{equationNumberStr}{delimiter}"

def fraction(numerator, denominator) -> str:
    """
    Params:
        numerator (any) : the numerator of the fraction
        denominator (any) : the denominator of the fraction

    Returns:
        latex (str) : the fraction written in LaTeX
    """
    return "\\frac{" + f"{numerator}" + "}{" + f"{denominator}" + "}"

def summation(indexName:str=None, start:int=None, end:str=None, expression:str=None) -> str:
    """
    Returns the sum expression written in LaTeX
    """
    indexStr = indexName if indexName != None else "i"
    startStr = f" = {start}" if start != None else ""
    endStr = str(end) if end != None else ""
    expressionStr = expression if expression != None else "x"

    index = indexStr + startStr

    return "\\sum^{" + endStr + "}_{" + index + "}{" + expressionStr + "_" + indexStr + "}"

def productory(indexName:str=None, start:int=None, end:str=None, expression:str=None) -> str:
    """
    Returns the product expression written in LaTeX
    """
    indexStr = indexName if indexName != None else "i"
    startStr = f" = {start}" if start != None else ""
    endStr = str(end) if end != None else ""
    expressionStr = expression if expression != None else "x"

    index = indexStr + startStr

    return "\\prod^{" + endStr + "}_{" + index + "}{" + expressionStr + "_" + indexStr + "}"

def tableContent(lines:list[tuple], columns:int, titles:tuple=None, scale:float=None):
    """
    Returns the lines organized in table content written in LaTeX\\
    This can then be passed to either "table()" or "tableSubfloat()"\\
    to make a single table or a list of tables respectively
    """
    latex = ""
    if scale != None: latex += "\\scalebox{" + f"{min(1, max(0, scale))}" + "}{%\n"
    latex += "\\begin{tabular}{" + f"{'|c' * columns}" + "|}\n"
    if titles != None:
        latex += "\t\\hline\n"
        latex += f"\t{' & '.join(map(str, titles))} \\\\\n"
    latex += "\t\\hline\n"
    
    for line in lines:
        latex += f"\t{' & '.join(map(str, line))} \\\\\n"
    
    latex += "\t\\hline\n"
    latex += "\\end{tabular}"
    if scale != None: latex += "\n}%"
    return latex

def table(tableContent:str, tableNumber:str=None, caption:str=None, label:str=None):
    """
    Returns the table content encapsulated in a table written in LaTeX
    """
    latex = "\\begin{table}[h]\n"
    latex += "\t\\captionsetup{labelformat=empty}\n"
    latex += "\t\\captionsetup[subfloat]{labelformat=empty}\n"
    latex += "\t\\centering\n"
    
    latex += f"{cu.tab(tableContent)}\n"

    tableNumberStr = f"Tabella {tableNumber}" if tableNumber != None else ""
    captionStr = f"{': ' if tableNumber != None else ''}{caption}" if caption != None else ""

    if tableNumberStr != "" or captionStr != "":
        latex += "\t\\caption{" + f"{tableNumberStr}{captionStr}" + "}\n"
    latex += "\\end{table}"
    if label != None: latex += "\n\\label{tab:" + f"{label}" + "}"

    return latex

def tableSubfloat(tableContents:list[str], subfloatCaptions:tuple=None, subfloatNumber:str=None, caption=None, label:str=None) -> str:
    """
    Returns the table contents encapsulated in set of table subfloats written in LaTeX
    """
    latex = "\\begin{table}[h]\n"
    latex += "\t\\captionsetup{labelformat=empty}\n"
    latex += "\t\\captionsetup[subfloat]{labelformat=empty}\n"
    latex += "\t\\centering\n"

    n = len(tableContents)
    if subfloatCaptions == None: subfloatCaptions = [""] * n
    else: subfloatCaptions = [f"\\centering {c}" for c in subfloatCaptions]

    for i in range(n):
        content = tableContents[i]
        latex += f"\t\\subfloat[{subfloatCaptions[i]}]" + "{\n"
        latex += f"{cu.tab(content)}\n"
        latex += "\t}\n"
        if i < n - 1: latex += "\t\\hfill\n"
    
    tableNumberStr = f"Tabelle {subfloatNumber}" if subfloatNumber != None else ""
    captionStr = f"{': ' if subfloatNumber != None else ''}{caption}" if caption != None else ""

    if tableNumberStr != "" or captionStr != "":
        latex += "\t\\caption{" + f"{tableNumberStr}{captionStr}" + "}\n"
    latex += "\\end{table}"
    if label != None: latex += "\n\\label{sub:" + f"{label}" + "}"

    return latex

def figure():
    #TODO
    pass

def errorPropagationFormula() -> str:
    """
    Returns the error propagation formula written in LaTeX
    """
    
    return "\\sigma_{f} = \\sqrt{\\sum^N_{i = 0}{ \\left( \\frac{\\partial f}{\\partial x_i} \\sigma_{x_i} \\right) ^2}}"


def varianceFormula(xName=None, N:int=None) -> str:
    """
    Returns the variance formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"
    
    return "\\sigma^2_{" + x + "} = \\frac{\\sum^{" + Nstr + "}_{i = 0}{({" + x + "}_i - \\overline{" + x + "}) ^ 2}}{" + Nstr + " - 1}"

def standardDeviationFormula(xName=None, N:int=None) -> str:
    """
    Returns the standard deviation formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"
    
    return "\\sigma_{" + x + "} = \\sqrt{\\frac{\\sum^{" + Nstr + "}_{i = 0}{({" + x + "}_i - \overline{" + x + "}) ^ 2}}{" + Nstr + " - 1}}"

######################################################################################################
def averageStandardDeviationFormula(xName=None, N:int=None) -> str:
    """
    Returns the average standard deviation formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"
    
    return "\\sigma_{\\overline{" + x + "}} = \\frac{\\sigma_{" + x + "}}{\\sqrt{"+ Nstr + "}}"

def averageFormula(xName=None, N:int=None) -> str:
    """
    Returns the average formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"

    return "\\overline{" + x + "}=\\frac{1}{" + Nstr + "}\\sum^{" + Nstr + "}_{i=0}{" + x + "_i}"

def weightedAverageFormula(xName=None, N:int=None) -> str:
    """
    Returns the weighted average formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"

    return "\\overline{" + x + "}=\\frac{\\sum^{" + Nstr + "}_{i=0}{" + x + "_iw_i}}{\\sum^{" + Nstr + "}_{i=0}{w_i}} \\quad\\quad\\quad w_i=\\frac{1}{\\sigma^2_i}"

def weightedAverageErrorFormula(xName=None, N:int=None) -> str:
    """
    Returns the weighted average error formula written in LaTeX
    """
    x = xName if xName != None else "x"
    Nstr = f"{N}" if N != None else "N"
    
    num = "\\sigma_{" + f"{x}" + "}"
    den = "\\sqrt{" + f"{Nstr}" + "}"
    
    return "\\sigma_{\\overline{" + x + "}}=\\frac{1}{\\sqrt{\\sum^{" + Nstr + "}_{i=0}{w_i}}} \\quad\\quad\\quad w_i = \\frac{1}{\\sigma^2_i}"