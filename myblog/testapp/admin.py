from django.contrib import admin

# Register your models here.

from testapp.models import Dog

class DogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dog, DogAdmin)
