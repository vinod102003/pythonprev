def convert_case(string):
    converted_string = ''
    for char in string:
        if char.islower():
            converted_string += char.upper()
        elif char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char
    return converted_string

# Test the function
sample_input = "I love PyTHon"
output = convert_case(sample_input)
print("Sample input:", sample_input)
print("Sample output:", output)
