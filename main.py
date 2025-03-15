import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*()-_+=]", password)

    # Calculate strength score (out of 5)
    strength_score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])
    
    # Strength level
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Feedback messages
    feedback = []
    if length_error:
        feedback.append("Password should be at least 8 characters long.")
    if uppercase_error:
        feedback.append("Password should contain at least one uppercase letter (A-Z).")
    if lowercase_error:
        feedback.append("Password should contain at least one lowercase letter (a-z).")
    if digit_error:
        feedback.append("Password should contain at least one digit (0-9).")
    if special_char_error:
        feedback.append("Password should contain at least one special character (!@#$%^&*()-_+=).")

    return {
        "password": password,
        "strength": strength,
        "score": strength_score,
        "feedback": feedback
    }

# Example Usage
if __name__ == "__main__":
    password = input("Enter a password: ")
    result = check_password_strength(password)

    print(f"\nPassword Strength: {result['strength']} ({result['score']}/5)")
    if result["feedback"]:
        print("Feedback:")
        for suggestion in result["feedback"]:
            print(f"- {suggestion}")
