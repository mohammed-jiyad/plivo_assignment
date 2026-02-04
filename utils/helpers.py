def normalize_number(number):
    """
    Normalizes phone numbers for safe comparison.
    Removes spaces, dashes, etc.
    """
    if not number:
        return ""
    return number.replace(" ", "").replace("-", "").strip()


def is_same_number(num1, num2):
    """
    Checks if two phone numbers are the same.
    Prevents self-transfer call loops.
    """
    return normalize_number(num1) == normalize_number(num2)
