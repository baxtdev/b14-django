from django.urls import path
from .views import main_page


urlpatterns = [
    path(route='',view=main_page,name="main-page")
]