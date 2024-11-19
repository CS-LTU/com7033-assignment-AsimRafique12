# utils/validators.py
from wtforms.validators import ValidationError

def validate_age(form, field):
    if field.data < 0 or field.data > 120:
        raise ValidationError("Age must be between 0 and 120.")