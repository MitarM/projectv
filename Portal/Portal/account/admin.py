from django.contrib import admin
from .models import Organizacija, Volonter, Drzava, Mesto, Ulica
# from django.contrib.auth.admin import UserAdmin

from import_export.admin import ImportExportModelAdmin

# Register your models here.

class IEAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

admin.site.register(Organizacija)
admin.site.register(Volonter)
admin.site.register(Drzava, IEAdmin)
admin.site.register(Mesto, IEAdmin)
admin.site.register(Ulica, IEAdmin)


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
