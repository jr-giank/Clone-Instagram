#Importaciones de Django
from django.contrib import admin

#Importaciones locales
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = 'user', 'phone_number', 'website', 'profile_picture'
    search_fields = 'user__email', 'user__first_name', 'user__last_name'