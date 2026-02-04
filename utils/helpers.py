def normalize_number(number):
    if not number:
        return ""

    # Remove spaces, dashes, brackets
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    return number.strip()


def is_same_number(num1, num2):
    return normalize_number(num1) == normalize_number(num2)
