from django.contrib import admin

from .models import neighbourhood,notifications,Profile,Business,Health,Authorities




# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Profile)
admin.site.register(notifications)
admin.site.register(Health)
admin.site.register(Business)
admin.site.register(Authorities)