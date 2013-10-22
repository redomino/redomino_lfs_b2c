from django.conf import settings

settings.SHOW_VAT = getattr(settings, 'SHOW_VAT', False)
settings.SHOW_VAT_IN_CART = getattr(settings, 'SHOW_VAT_IN_CART', False)


