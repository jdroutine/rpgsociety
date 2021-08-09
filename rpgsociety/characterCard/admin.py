from django.contrib import admin
from .models import Character, Gallery, Home, Map

# Register your models here.
admin.site.register(Character)
admin.site.register(Home)
admin.site.register(Map)
admin.site.register(Gallery)