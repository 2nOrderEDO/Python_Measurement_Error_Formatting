import numpy as np

def format_error(value, error):
    # Rounding method used is banker's rounding
    
    error = np.format_float_scientific(error, 0) # print error as sci. notation rounding
    digits, exp = error.split('e') # extract digits and exponent
    decimals = abs(int(exp)) if int(exp) <= 0 else 0
    digits = np.around(float(digits))
    value = np.around(value, -int(exp)) # adjust significant digits to the ones allowed by the error.
    output_string = '{:.'+str(decimals)+'f} ±{:.'+str(decimals)+'f}'
    
    return output_string.format(value, digits * 10 ** int(exp)) #return formatted string
