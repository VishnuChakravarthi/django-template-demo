from django.urls import path

from template_app import views

app_name = 'basic_app'

urlpatterns = [
    path('second', views.second_page, name="second"),
    path('third', views.third_page, name="third")
]
