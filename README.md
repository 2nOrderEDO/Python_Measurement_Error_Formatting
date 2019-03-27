# Python Error Formatting function

This function takes two floats, a **value** and its **error/uncertainity** (145.7 and 3.4) and returns a **string** with scientific format (146 ± 3) showing one significant digit error and the correct number of significant digits for the value given the specified error.

Example: | Output
---|---
format_error(100, 1) | 100 ±1
format_error(100, 0.001) | 100.000 ±0.001
format_error(3.418, 0.123) | 3.4 ±0.1
format_error(6.3, 0.09) | 6.30 ±0.09
format_error(46288, 1551) | 46000 ±2000
format_error(428.351, 0.27) | 428.4 ±0.3
format_error(0.01683, 0.0058) | 0.017 ±0.006
