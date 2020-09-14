from django.urls import path
from django.views.generic import TemplateView

from api import views

urlpatterns = [
    path('', views.ListTitleView.as_view(), name='title'),
    path('seasons/', views.ListSeasonsView.as_view(), name='list-seasons'),
    path('seasons/<int:id>', views.EpisodesListView.as_view(), name='get-season'),
    path('seasons/<int:season>/episode/<int:episode>', views.EpisodesDetailView.as_view(), name='get-episode'),
    path('seasons/<int:season>/episode/<int:episode>/comment', views.CommentView.as_view(), name='comment'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
]
