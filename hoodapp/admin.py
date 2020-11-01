from django.contrib import admin

from .models import neighbourhood,notifications,Profile




# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Profile)
admin.site.register(notifications)