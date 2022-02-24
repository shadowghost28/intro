from django.urls import path
from .views import BlogListView, BlogCreateView

app_name="blog"

urlpatterns = [
   path('', BlogListView.as_view(), name="home"),  #siempre esta coma,...
   path('create/', BlogCreateView.as_view(), name="create")
]
