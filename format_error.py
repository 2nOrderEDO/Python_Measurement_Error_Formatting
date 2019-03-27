import numpy as np

def format_error(value, error):
    error = np.format_float_scientific(error, 0) # print error as sci. notation
    digits = float(error.split('e')[0]) # extract digits
    exp = int(error.split('e')[1]) # extract exponent
    if exp <= 0: 
        decimals = abs(exp) 
    else:
        decimals = 0 #
    digits = np.around(digits)
    value = np.around(value, -exp)           
    tmp = '{:.'+str(decimals)+'f} ±{:.'+str(decimals)+'f}'
    
    return tmp.format(value, digits*10**exp)
