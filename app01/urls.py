from django.urls import path
from app01.views import *

urlpatterns = [
    path('', index, name="index"),
    path('create_blog/', create_blog, name="create_blog"),
    path('modify_blog/<int:id>', modify_blog, name="modify_blog"),    
]