from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    def ready(self):
        try:
            from django.contrib.auth.models import User
            users = User.objects.count()
            if(users == 0):
                print("Admin doesn't exist, creating")
                User.objects.create_superuser("Administrator", "emanuele.giordano@admin.it", "Password2023!!")
        except: 
            pass
        