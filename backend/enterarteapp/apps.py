from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
<<<<<<<< HEAD:backend/enterarteapp/apps.py
    name = 'enterarteapp'


    def ready(self):
        import enterarteapp.signals  # Importa las señales
========
    name = 'apps.account'
>>>>>>>> develop:backend/apps/account/apps.py
