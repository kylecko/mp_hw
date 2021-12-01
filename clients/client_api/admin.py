# Register your models here.

from django.contrib import admin
from .models import File, Provider
#from Files.models import File, FileType

class FileAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "phone_number", "client_member_id", "account_id"]


admin.site.register(File)
admin.site.register(Provider)
admin.site.register(File, FileAdmin)

