from scripts import console_utils as cu

def number(number:float, unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str:
    delimiter = "$$" if centered else "$"
    nameStr = f'{name} = ' if name != None else ''
    numberStr = cu.roundScientific(number, significant_figures, False, force_scientific_notation)
    unitStr = unit if unit != None else ''
    return f"{delimiter}{nameStr}{numberStr}{unitStr}{delimiter}"

def measure(measure:tuple[float], unit:str=None, name:str=None, significant_figures:int=None, force_scientific_notation:bool=False, centered:bool=False) -> str:
    delimiter = "$$" if centered else "$"
    measureStr = cu.get_value_errors_from_tuple(measure, unit, name, significant_figures, force_scientific_notation).replace("±", "\\pm")
    return f"{delimiter}{measureStr}{delimiter}"

def table(data:list[tuple], columns:int, titles:tuple=None, label:str=None, tableNumber:int=None, caption:str=None) -> str:
    latex = """\\begin{table}[h]
        \\captionsetup{labelformat=empty}
        \\centering
        """
    latex += "\\begin{tabular}{" + "|c" * columns + "|}\n"

    if titles != None:
        t = map(str, titles)
        latex += "\t\t\\hline\n\t\t\\textbf{" + "} & \\textbf{".join(t) + "} \\\\\n\t\t\\hline\n"

    for d in data:
        d = map(str, d)
        latex += "\t\t" + " & ".join(d) + "\\\\\n"

    latex += "\t\t\\hline\n\t\\end{tabular}"
    tableNumberStr = (f" {tableNumber}" if tableNumber != None else "")
    captionStr = (f"{caption}" if caption != None else "")
    latex += "\n\t\\caption{Tabella" + tableNumberStr + ": " + captionStr + "}"
    if label != None: latex += "\n\\label{tab:" + f"{label}" + "}"
    latex += "\n\\end{table}"
    
    return latex

# columns = 4

# lines = []
# with open("./dati.txt", "r") as f:
#     lines = f.readlines()

#     latex = """\\begin{table}[h]
#         \\captionsetup{labelformat=empty}
#         \\centering
#         """
#     latex += "\\begin{tabular}{" + "|c|" * columns + "}\n"

#     # fill with datat


#     latex += "\t\\end{tabular}"
#     latex += "\t\\caption{Tabella {n}: {caption}}"
#     latex += """
#         \\label{tab:{label}}
#     \\end{table}"""

# def table(columns:int, content:list[list]):
#     output = """\\begin{table}[h]
#         \\captionsetup{labelformat=empty}
#         \\centering
#         """
#     for line in content:
#         if len(line) > columns:
#             print("[Error]: Invalid content format. A line contains more columns then expected!")
#             return "INVALID TABLE"
#         output += " & ".join(map(str, line)) + "\\\\\n"
#     output += "\t\\end{tabular}"
#     if table_number != None: output += "\t\\caption{Tabella " + f"{table_number}"
#     if caption != None: output += ": {caption} + "}"
#     output += """
#     \\label{tab:{label}}
#     \\end{table}"""