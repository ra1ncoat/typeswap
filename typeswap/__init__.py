# Created by Pyto

"""
Swap variable types fast!
"""

def changetype(variable, type):
    if type == "float":
        output = float(variable)
    
    elif type == "int":
        output = int(variable)
        
    elif type == "str":
        output = str(variable)
    
    elif type == "e":
        for char in variable:
            output += char + "e"
  
    else:
        output = "Invalid type."

    return output
        