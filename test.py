import re

def validate_float(input_string):
    pattern = "^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$"
    if re.match(pattern, input_string) or re.match("^[-+]?(\d+[eE][-+]?\d+)$", input_string):
        return f"{input_string} is legal."
    else:
        return f"{input_string} is illegal."

# пример использования
inputs = ["1.2", "1", "1e-55", "e-12", "6.5E", "1e-12", "+4.1234567890E-99999", "7.6e+12.5", "99"]
for input_string in inputs:
    print(validate_float(input_string))