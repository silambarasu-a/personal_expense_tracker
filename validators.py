from datetime import datetime


class ValidationError(ValueError):
    """Raised when a value fails validation. Carries a user-friendly message."""
    pass


def validate_required_text(value, field_name="Value"):
    """Ensure text is non-empty after stripping; return the cleaned text."""
    value = value.strip()
    if not value:
        raise ValidationError(f"{field_name} cannot be empty.")
    return value


def validate_amount(value):
    """Ensure the value is a number greater than zero; return it as a float."""
    try:
        amount = float(value)
    except (ValueError, TypeError):
        raise ValidationError("Amount must be a numeric value.")
    if amount <= 0:
        raise ValidationError("Amount must be greater than zero.")
    return amount


def validate_choice(value, options):
    """Ensure the value is a valid 1-based index into options; return the chosen option."""
    try:
        choice = int(value)
    except (ValueError, TypeError):
        raise ValidationError("Please enter a numeric value.")
    if not 1 <= choice <= len(options):
        raise ValidationError(f"Please enter a number between 1 and {len(options)}.")
    return options[choice - 1]


def validate_date(value):
    """Ensure the value matches YYYY-MM-DD; return the cleaned date string."""
    value = value.strip()
    if not value:
        raise ValidationError("Date cannot be empty.")
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise ValidationError("Invalid date format. Please use YYYY-MM-DD.")
    return value
