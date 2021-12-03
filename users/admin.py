from django.contrib import admin

class UsersAdmin(admin.ModelAdmin):
    list_display = ['name']
