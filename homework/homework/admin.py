from django.contrib import admin
from homework.models import ENTRY

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(ENTRY, )