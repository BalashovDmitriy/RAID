from django.urls import path

from main.views import FrameworkListAPIView, FrameworkListByLanguageAPIView, FrameworkCreateAPIView

urlpatterns = [
    path('frameworks/create/', FrameworkCreateAPIView.as_view(), name='framework-create'),
    path('frameworks/', FrameworkListAPIView.as_view(), name='framework-list-all'),
    path('frameworks/<str:language>/', FrameworkListByLanguageAPIView.as_view(), name='framework-list-by-language')
]
