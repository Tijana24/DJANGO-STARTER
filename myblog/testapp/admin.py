from django.contrib import admin

# Register your models here.

from testapp.models import Dog

class DogAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dog, DogAdmin)


from testapp.models import Cat

class CatAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cat, CatAdmin)