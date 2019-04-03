# Python Error Formatting function

This function takes two floats, a **value** and its **error/uncertainity** (145.7 and 3.4) and returns a **string** with scientific format (146 ± 3) showing one significant digit error and the correct number of significant digits for the value given the specified error.


|Example: | Output|
|---|---|
|format_error(100, 1) | 100 ±1|
|format_error(100, 0.001) | 100.000 ±0.001|
|format_error(3.418, 0.123) | 3.4 ±0.1|
|format_error(6.3, 0.09) | 6.30 ±0.09|
|format_error(46288, 1551) | 46000 ±2000|
|format_error(428.351, 0.27) | 428.4 ±0.3|
|format_error(0.01683, 0.0058) | 0.017 ±0.006|


```python

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
```


