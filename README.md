# Python_Measurement_Error_Formating

Give this function a value and its error (145.7 and 3.4) and returns the correct scientific format (146 ± 3)  with one significant digit

Example:

print(format_error(100, 1))           # 100 ±1

print(format_error(100, 0.001))       # 100.000 ±0.001

print(format_error(3.418, 0.123))     # 3.4 ±0.1

print(format_error(6.3, 0.09))        # 6.30 ±0.09

print(format_error(46288, 1551))      # 46000 ±2000

print(format_error(428.351, 0.27))    # 428.4 ±0.3

print(format_error(0.01683, 0.0058))  # 0.017 ±0.006

