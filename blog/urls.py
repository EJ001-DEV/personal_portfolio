from django.urls import path
from .views import render_post, post_detail

app_name = "blog"

urlpatterns = [
    path("", render_post, name="posts"),#este es el path origen de urls.py dentro de la app "post", esta url viene redirigida desde la url del proyecto "django_portfolio". Nota: debe importar la vista desde .views y path desde django.urls    
    path('<int:post_id>', post_detail, name='post_detail'),
]
