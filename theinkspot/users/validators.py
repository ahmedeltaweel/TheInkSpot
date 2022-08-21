from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_facebook(value):
    if '.' in value and \
           value.split('.', 1)[1].lower() in "facebook":
           raise ValidationError(_("URL isn't Facebook related."))
