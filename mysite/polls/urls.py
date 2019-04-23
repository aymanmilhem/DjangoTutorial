from django.urls import path

from . import views

<<<<<<< HEAD
app_name = 'polls'
urlpatterns = [
=======
# new, added to use django's generic views in part 4
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# old
"""
urlpatterns = [
>>>>>>> 010bdff1dae236696ac9f2ee89cc4df822545844
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
<<<<<<< HEAD
    # ex: /polls/5/vote/
=======
    # ex: /polls/5/vote
>>>>>>> 010bdff1dae236696ac9f2ee89cc4df822545844
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
"""
