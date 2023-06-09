from django.contrib import admin

# Register your models here.
from .models import Animal, Species, Domain, Kingdom, Phylum, Class, Order, Family, Genus


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'parent_group', 'height', 'lifespan',)


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'weight', 'parent_group', 'height', 'lifespan',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species)
admin.site.register(Domain)
admin.site.register(Kingdom)
admin.site.register(Phylum)
admin.site.register(Class)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)





