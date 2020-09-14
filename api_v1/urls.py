from django.urls import path

from api_v1 import views

urlpatterns = [
    path('', views.ListTitleView.as_view(), name='title'),
    path('seasons/', views.ListSeasonsView.as_view(), name='list-seasons'),
    path('seasons/<int:id>', views.EpisodesListView.as_view(), name='get-season'),
    path('seasons/<int:season>/episode/<int:episode>', views.EpisodesDetailView.as_view(), name='get-episode'),
    path('seasons/<int:season>/episode/<int:episode>/comment', views.CommentView.as_view(), name='comment')
]
