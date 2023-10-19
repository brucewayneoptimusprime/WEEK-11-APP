def check_password_strength(password):
    # Define criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()" for char in password)

    # Check each criteria
    strength = "Weak"
    if length_criteria and uppercase_criteria and lowercase_criteria and digit_criteria and special_char_criteria:
        strength = "Strong"
    elif length_criteria and (uppercase_criteria or lowercase_criteria or digit_criteria):
        strength = "Moderate"

    return strength

# Example usage:
password = "P@ssw0rd"
strength = check_password_strength(password)
print(f"The password is {strength}.")
