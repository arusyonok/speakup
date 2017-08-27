from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fields = ['name', 'surname', 'email', 'age', 'gender', 'occupation']
    list_display = ('full_name', 'email', 'age', 'gender', 'occupation')


admin.site.register(User, UserAdmin)