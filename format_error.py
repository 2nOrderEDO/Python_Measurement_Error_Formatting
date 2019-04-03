import numpy as np

def format_error(value, error):
    #Rounding method used is banker's rounding
    
    error = np.format_float_scientific(error, 0) # print error as sci. notation rounding
    digits = float(error.split('e')[0]) # extract digits
    exp = int(error.split('e')[1]) # extract exponent
    if exp <= 0: 
        decimals = abs(exp) # show as many decimals as positions after decimal separator
    else:
        decimals = 0 # do not show decimals 
    digits = np.around(digits) 
    value = np.around(value, -exp) # adjust significant digits to the ones allowed by the error.     
    
    output_string = '{:.'+str(decimals)+'f} ±{:.'+str(decimals)+'f}'
    
    return output_string.format(value, digits*10**exp) #return formatted string
