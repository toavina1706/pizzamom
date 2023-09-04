from django.urls import path
from . import views

app_name = 'menu'   #ilaina rehefa mapiasa lien ifandraisana
#lien ifandraisan'ny view amin HTML. creena ito fichier ito de apifandraisina amin urls principale
urlpatterns = [
    path("", views.index, name="index"),
]
