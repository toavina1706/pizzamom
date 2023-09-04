from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):                  #modifier l'affichage classement donnees sur l'interface admin
    list_display =("nom","ingredients","vegetarienne","prix")
    search_fields = ["nom"]


admin.site.register(Pizza, PizzaAdmin)

