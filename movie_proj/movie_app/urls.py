from . import views
from django.urls import path
from .views import ListFeedBack, DetailFeedBack

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name = 'movie-detail'),
    path('directors/', views.show_directors),
    path('directors/<int:id_dir>', views.one_dir, name = 'one_dir'),
    path('actors/', views.show_actors),
    path('actors/<int:id_dir>', views.info_actor, name='one_actor'),
    path('actors/list', ListFeedBack.as_view()),
    path('detail/<int:pk>', DetailFeedBack.as_view()),
]