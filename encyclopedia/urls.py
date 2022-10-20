from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name ="index"),
    path('search', views.search, name ="search"),
    path('create_page', views.create_page, name ="create_page"),
    path('<str:title_name>/edit', views.edit, name="edit"),
    path('update', views.update, name="update"),
    path('random_page', views.random_page, name ="random_page"),
    path('<str:title>', views.title, name ="title")
]

