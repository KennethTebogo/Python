#Part 1:Python Tutorial
# Create a list of weights in kg.
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package as np
import numpy as np

# Create a numpy array np_weight_kg from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
np_weight_lbs = np_weight_kg * 2.2046

# Print out np_weight_lbs
print(np_weight_lbs)


#Part 2:Challenges
def longest_alternating_substring(s):
    """
    Function to find the longest substring with alternating odd/even or even/odd digits.
    
    Args:
    s (str): A string of digits.

    Returns:
    str: The longest substring with alternating odd and even digits.
    """
    
    def is_odd(digit):
        """
        Helper function to check if a digit is odd.
        
        Args:
        digit (str): A single character representing a digit.

        Returns:
        bool: True if the digit is odd, False otherwise.
        """
        return int(digit) % 2 != 0
    
    def is_even(digit):
        """
        Helper function to check if a digit is even.
        
        Args:
        digit (str): A single character representing a digit.

        Returns:
        bool: True if the digit is even, False otherwise.
        """
        return int(digit) % 2 == 0

    # Initialize variables to keep track of the maximum length substring
    max_length = 0
    max_substring = ""
    start = 0  # Start index of the current alternating substring

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        # Check if the current digit alternates in parity with the previous digit
        if (is_odd(s[i]) and is_even(s[i - 1])) or (is_even(s[i]) and is_odd(s[i - 1])):
            # Continue the current alternating substring
            current_length = i - start + 1
        else:
            # End of the current alternating substring
            current_length = i - start
            # Check if the length of the current substring is greater than the max found so far
            if current_length > max_length:
                max_length = current_length
                max_substring = s[start:i]
            # Reset the start index for the next potential alternating substring
            start = i

    # After the loop, check the last substring from the last start index to the end of the string
    current_length = len(s) - start
    if current_length > max_length:
        max_length = current_length
        max_substring = s[start:]

    return max_substring

print(longest_alternating_substring("225424272163254474441338664823"))
print(longest_alternating_substring("594127169973391692147228678476")) 
print(longest_alternating_substring("721449827599186159274227324466")) 
