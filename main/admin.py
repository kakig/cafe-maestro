from django.contrib import admin

from .models import Usuario, Plantacao, Insumo

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Plantacao)
admin.site.register(Insumo)
