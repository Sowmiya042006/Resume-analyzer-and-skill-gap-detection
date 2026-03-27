import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError(
                _("This password must contain at least 8 characters."),
                code='password_too_short',
            )
            
        if not re.search(r'[a-zA-Z]', password):
            raise ValidationError(
                _("This password must contain at least 1 letter."),
                code='password_no_letters',
            )
            
        if not re.search(r'\d', password):
            raise ValidationError(
                _("This password must contain at least 1 digit."),
                code='password_no_digits',
            )
            
        if not re.search(r'[^a-zA-Z\d\s:]', password):
            raise ValidationError(
                _("This password must contain at least 1 special character."),
                code='password_no_special_chars',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 8 characters, 1 letter, 1 digit, and 1 special character."
        )
