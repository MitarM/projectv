from django.contrib import admin
from .models import Organizacija, Volonter
# from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(Organizacija)
admin.site.register(Volonter)

# from .models import User
#
# class CustomUserAdmin(UserAdmin):
#     pass
#
# admin.site.register(User, CustomUserAdmin)

# class OrganizacijaInline(admin.StackedInline):
#     model = Organizacija
#     can_delete = False
#     verbose_name_plural = 'organisations'
#
# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (OrganizacijaInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
