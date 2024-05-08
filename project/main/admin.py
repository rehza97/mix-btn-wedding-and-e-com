from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Salle)
admin.site.register(Product)
admin.site.register(CameraTeam)
admin.site.register(Reservation)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ExtraService)
admin.site.register(ExtraServiceSalle)

