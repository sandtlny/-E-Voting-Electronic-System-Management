rom django.urls import path
from .views import register, user_login, vote, results

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('vote/', vote, name='vote'),
    path('results/', results, name='results'),
]