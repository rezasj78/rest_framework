from django.urls import path
from . import views

urlpatterns = [
    path('', views.StatusApiListCreateView.as_view()),
    path('<int:id>/', views.StatusApiDetailView.as_view()),
    # path('all/', views.StatusAllRequestsApiView.as_view()),
    # path('create/', views.StatusCreateApiView.as_view()), TODO
    # path('<int:id>/update/', views.StatusUpdateApiView.as_view()),
    # path('<int:id>/delete/', views.StatusDeleteApiView.as_view()),
]