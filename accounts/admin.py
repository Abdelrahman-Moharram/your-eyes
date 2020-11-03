from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.users)
admin.site.register(models.Category)
admin.site.register(models.doctor)
admin.site.register(models.Disease)
admin.site.register(models.FamilyDisease)
admin.site.register(models.patient)

