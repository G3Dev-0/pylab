def roundScientific(number:float, significantFigures:int, putDotAfterFirstDigit:bool=False, forceScientificNotation:bool=False):
    """
    Rounds a number to a specific number of significant figures.
    Unless scientific notation use is forced, the algorithm will use it only in the following cases:
    - rounding 321 to 2 significant figures -> 32 * 10 ^ 1
    - rounding 99.9 to 2 significant figures -> 10 * 10 ^ 1

    Params:
        number (float): the number to round
        significantFigures (int): the number of significant figures
        putDotAfterFirstDigit (bool): if scientific notation is needed, the decimal dot will be put after the first non-zero digit
        forceScientificNotation (bool): forces the program to use the scientific notation where possible. In this case, the decimal dot will be ALWAYS put after the first non-zero digit

    Returns:
        roundedNumber (str): the rounded number
    """
    if number == 0: return f"0.0"

    # turn the number into a string
    numberString = str(number)

    # strip away the minus to simplify calculations...it will be added back again on return
    negative = False
    if number < 0:
        negative = True
        numberString = numberString[1:]

    # count sigs
    sigs = 0
    canIncrement = False
    i = -1
    for d in numberString:
        i += 1
        if d == ".": continue
        if d != "0" and not canIncrement:
            canIncrement = True
            firstSig = i
        if canIncrement: sigs += 1

    # begin rounding the number
    roundedNumber = ""
    tenPower = ""

    # used later
    hasAddedASigDigitByRounding = False

    # if there are less sigs than the required ones add trailing zeros
    if sigs < significantFigures: roundedNumber = f"{numberString}{'0' * (significantFigures - sigs)}"
    # if there is the same number of sigs as the required ones return the given number
    elif sigs == significantFigures: roundedNumber = numberString
    # if there are more sigs than the required ones round and return
    else:
        # round
        # put digits into a list only to the number of required sigs
        end = firstSig + significantFigures
        # take one more digit if a dot in included into the sig digits space
        if numberString[end] == ".": end += 1
        #if "." in ns[firstSig:end]: end += 1
        digits = list(numberString)[:end]
        # increase them from the end to the start in a cascade in the digits after is >= 5
        if int(numberString[end]) >= 5:
            hasAddedASigDigitByRounding = False
            for i in range(len(digits) - 1, -1, -1):
                if digits[i] == ".": continue
                # increase the current digit
                digits[i] = str(int(digits[i]) + 1)
                #print(digits, hasRoundedToTenOnce)
                if digits[i] == "10":
                    # replace the 10s with 0s except for the first one, in that case also remove a trailing digit
                    if digits[i] == "10" and i > 0: digits[i] = "0"
                    # a new significative digit is added if a 9 gets rounded to a 10 in the place of the first significant figure
                    if i == firstSig: hasAddedASigDigitByRounding = True
                # stop increasing the digits if no more roundings are needed
                else: break
            
            # remove trailing zeros
            if hasAddedASigDigitByRounding: del digits[-1]

        # get the rounded number by joining together the digits
        roundedNumber = "".join(digits)

    # use scientific notation if the number couldn't be rounded
    
    # get the number of digits before the dot
    if "." in numberString: nonDecimalsBeforeRounding = len(numberString[:numberString.index(".")])
    # if there is no dot then every digit is a non decimal digit
    else: nonDecimalsBeforeRounding = len(numberString)
    
    # get the number of digits before the dot
    if "." in roundedNumber: nonDecimalsAfterRounding = len(roundedNumber[:roundedNumber.index(".")])
    # if there is no dot then every digit is a non decimal digit
    else: nonDecimalsAfterRounding = len(roundedNumber)

    appliedScientificNotation = False

    # use scientific notation in needed
    # this is the case 321 (2) -> 32 * 10 ^ 1
    if not forceScientificNotation and nonDecimalsAfterRounding < nonDecimalsBeforeRounding:
        # set the right power of ten
        exp = nonDecimalsBeforeRounding - nonDecimalsAfterRounding
        # move the dot after the first digit and thus update the exponent
        if putDotAfterFirstDigit:
            prevDotPos = nonDecimalsAfterRounding
            newDotPos = 1
            # moving the dot
            roundedNumber = roundedNumber[:newDotPos] + "." + roundedNumber[newDotPos:]
            # adding the moved distance to the exponent
            exp += prevDotPos - newDotPos
        tenPower = f" * 10 ^ {exp}"

        appliedScientificNotation = True
    # this is the case 99 (2) -> 10 * 10 ^ 1
    elif not forceScientificNotation and nonDecimalsAfterRounding > nonDecimalsBeforeRounding and nonDecimalsAfterRounding > significantFigures:
        # set the right power of ten
        exp = nonDecimalsAfterRounding - nonDecimalsBeforeRounding
        roundedNumber = roundedNumber[:nonDecimalsBeforeRounding]
        # move the dot after the first digit and thus update the exponent
        if putDotAfterFirstDigit:
            prevDotPos = nonDecimalsAfterRounding - 1
            newDotPos = 1
            # moving the dot
            roundedNumber = roundedNumber[:newDotPos] + "." + roundedNumber[newDotPos:]
            # adding the moved distance to the exponent
            exp += prevDotPos - newDotPos
        tenPower = f" * 10 ^ {exp}"

        appliedScientificNotation = True
    
    # this will work on decimals-only numbers and it will ALWAYS put the dot after the first digit
    if forceScientificNotation and not appliedScientificNotation:
        # find the first non zero digit
        i = 0
        for d in list(roundedNumber):
            if d != "0" and d != ".":
                firstSig = i
                break
            i += 1

        # moving the dot to the first position
        firstNonZeroDigitPos = firstSig

        steps = 0
        # also count the missing digits in case of numbers like 321 (2) -> 32 * 10 ^ 1
        if nonDecimalsAfterRounding < nonDecimalsBeforeRounding:
            steps = nonDecimalsBeforeRounding - 2

        # cut the number if there are too many significant digits (this is the case 99 (2) -> 10 * 10 ^ 1)
        if nonDecimalsAfterRounding > nonDecimalsBeforeRounding and nonDecimalsAfterRounding > significantFigures:
            roundedNumber = roundedNumber[:nonDecimalsBeforeRounding]
            # if a cut is made, you have to make sure you're including the cut digits into the exponent
            steps = nonDecimalsAfterRounding - nonDecimalsBeforeRounding

        #print(roundedNumber)
        shouldAddDot = not "." in roundedNumber
        includesDot = 0

        if shouldAddDot:
            roundedNumber = roundedNumber[firstNonZeroDigitPos] + "." + roundedNumber[firstNonZeroDigitPos + 1:]
        
        if roundedNumber[0] == "0":
            roundedNumber = roundedNumber[firstNonZeroDigitPos] + "." + roundedNumber[firstNonZeroDigitPos + 1:]
            if not shouldAddDot: includesDot = 1

        # set the right power of ten
        exp = -firstNonZeroDigitPos + (1 if shouldAddDot else 0) + steps + includesDot
        tenPower = f" * 10 ^ {exp}"

    # remove trailing dots
    if roundedNumber[-1] == ".": roundedNumber = roundedNumber[:-1]

    # remove 10 ^ 0
    if "^ 0" in tenPower: tenPower = ""

    return f"{'-' if negative else ''}{roundedNumber}{tenPower}"

def get_value_errors_from_tuple(measure:tuple[float], unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False):
    """
    Creates a format string with the that shows a measurement in a simple way.\\
    The f-string pattern is the following:\\
    "{name} = ({value_0} ± {error_0}){unit}"

    Params:
        measure (tuple[float]) : the measurement to put in the string. The tuple MUST contain the pair (value, error)
        unit (str) : the measurement unit

    Returns:
        output (str) : a format string displaying the measure
    """
    if name == None: name = ""
    else: name += " = "

    if unit == None: unit = ""

    value = measure[0]
    error = measure[1]
    
    if significant_figures != None: value = roundScientific(value, significant_figures, False, force_scientific_notation)
    if significant_figures != None: error = roundScientific(error, significant_figures, False, force_scientific_notation)
    return f"{name}({value} ± {error}){unit}"

def get_value_errors_from_list(measurements:list[tuple[float]], units:list[str]=None, names:list[str]=None, separator:str=" ", ending:str="", significant_figures:int=None, force_scientific_notation:bool=False):
    """
    Creates a format string with the that shows a set of measurements in a simple way.\\
    The f-string pattern is the following:\\
    "{name_i} = ({value_i} ± {error_i}){unit_i}{separator}"\\ (if all names are given)
    or \\
    "{name}_i = ({value_i} ± {error_i}){unit_i}{separator}"\\ (if only one name is given it will iterate through by assign a number)
    Ends with {ending}\\
    \\
    SUPPORTS DIFFERENT UNITS FOR EACH MEASURE

    Params:
        measurements (list[tuple[float]]) : the measurements to put in the string. Every tuple MUST contain the pair(s) (value, error)
        units (list[str]) : the measurements units
        names (list[str]) : the measurements names
        separator (str) : a char sequence that separates the measures
        ending (str) : a char sequence to end the string with

    Returns:
        output (str) : a format string displaying all the measures
    """
    if units == None: units = [""] * len(measurements)
    if len(units) == 1: units = [units[0]] * len(measurements)

    if len(names) == 1: names = [names[0]] * len(measurements)
    if names == None: names = [""] * len(measurements)
    else: names = [name + " = " for name in names]

    output = ""
    for i in range(len(measurements)):
        value = measurements[i][0]
        error = measurements[i][1]
        
        if significant_figures != None: value = roundScientific(value, significant_figures, False, force_scientific_notation)
        if significant_figures != None: error = roundScientific(error, significant_figures, False, force_scientific_notation)
        
        output += f"{names[i]}({value} ± {error}){units[i]}{separator}"
    return output.strip() + ending
"""
def get_value_errors_from_list(measurements:list[tuple[float]], unit:str="", name:str="", separator:str=" ", ending:str=""):
    ""
    Creates a format string with the that shows a set of measurements in a simple way.\\
    The f-string pattern is the following:\\
    "{name}_i = ({value_i} ± {error_i}){unit}{separator}"\\
    Ends with {ending}

    Params:
        measurements (list[tuple[float]]) : the measurements to put in the string. Every tuple MUST contain the pair(s) (value, error)
        unit (str) : the measurements unit
        name (str) : the measurements name
        separator (str) : a char sequence that separates the measures
        ending (str) : a char sequence to end the string with

    Returns:
        output (str) : a format string displaying all the measures
    ""
    output = ""
    n = 0
    for measure in measurements:
        output += f"{name}_{n} * ({measure[0]} ± {measure[1]}){unit}{separator}"
        n += 1
    return output.strip() + ending
"""
def tab(text:str, tabs:int=1):
    """
    Tabs a text by adding a customizable number of tabs at the beginning of every line in the given text

    Params:
        text (str) : the text to tab
        tabs (int) : the number of tabs to put before each line

    Returns:
        output (str) : the tabbed text
    """
    tt = ("\t" * tabs)
    return tt + text.replace("\n", "\n" + tt)