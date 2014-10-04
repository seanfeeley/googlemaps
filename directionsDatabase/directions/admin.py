from django.contrib import admin

from directions.models import *

admin.site.register(Location)
admin.site.register(LocationInArea)
admin.site.register(Area)
admin.site.register(Departure)
admin.site.register(Path)

# Register your models here.
