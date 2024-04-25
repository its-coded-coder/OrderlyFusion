from django.contrib import admin
from .models import CustomUser


# Register the Token model with the admin
admin.site.register(CustomUser)