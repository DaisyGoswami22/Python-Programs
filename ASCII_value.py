# Get user input for a character
char_input = input("Enter a character: ")

# Ensure the input is a single character
if len(char_input) == 1:
    # Use ord() to get the ASCII value
    ascii_value = ord(char_input)
    
    # Print the result
    print(f"The ASCII value of '{char_input}' is {ascii_value}")
else:
    print("Please enter only one character.")